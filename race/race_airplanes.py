import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

from race.config.airplane_config import AirplaneConfig
from race.models.airplane_race import Airplane


class RaceSimulation:
    def __init__(self):
        t = np.arange(0, 2.005, 0.005)

        # Aquí defines la carrera. Agregar un 4to avión es una línea.
        configs = [
            AirplaneConfig(a=800, n=1, altitude=2.5, color='r', label='Race 1'),
            AirplaneConfig(a=1600/2**0.5, n=0.5, altitude=1.5, color='b', label='Race 2'),
            AirplaneConfig(a=200, n=3, altitude=0.5, color='g', label='Race 3'),
        ]

        self.airplanes = [Airplane(c, t) for c in configs]
        self.t = t

        # Figura
        self.fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
        gs = gridspec.GridSpec(2,2)
        self.ax_map = self.fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))
        self.ax_dist = self.fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
        self.ax_vel = self.fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))

        self._setup_axes()
        self._create_lines()

    def _setup_axes(self):
        self.ax_map.set(xlim=(0, 1600), ylim=(0, 3), xlabel='x-distance', ylabel='y-distance', title='Airplane Race')
        self.ax_dist.set(xlim=(0, 2), ylim=(0, 1600), xlabel='time [hrs]', ylabel='x-distance [km]', title='X-distance VS time')
        self.ax_vel.set(xlim=(0, 2), ylim=(0, 1600), xlabel='time [hrs]', ylabel='speed [km/hr]', title='Speed vs time')
        for ax in [self.ax_map, self.ax_dist, self.ax_vel]:
            ax.grid(True)

    def _create_lines(self):
        # Líneas de las gráficas inferiores
        self.dist_lines = []
        self.vel_lines = []
        for ap in self.airplanes:
            l1, = self.ax_dist.plot([], [], f'-{ap.config.color}', lw=3, label=f"X={int(ap.config.a)}*t^{ap.config.n}")
            l2, = self.ax_vel.plot([], [], f'-{ap.config.color}', lw=3, label=f"V={ap.config.n*ap.config.a:.1f}*t^{ap.config.n-1:.1f}")
            self.dist_lines.append(l1)
            self.vel_lines.append(l2)

        self.ax_dist.legend()
        self.ax_vel.legend()

        self.map_artists = []
        for ap in self.airplanes:
            self.map_artists.extend(ap.create_artists(self.ax_map))

    def update(self, frame):
        for ap in self.airplanes:
            ap.update_artists(frame)

        for ap, dl, vl in zip(self.airplanes, self.dist_lines, self.vel_lines):
            dl.set_data(self.t[:frame], ap.x[:frame])
            vl.set_data(self.t[:frame], ap.v[:frame])

        return [*self.map_artists, *self.dist_lines, *self.vel_lines]

    def run(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=len(self.t), interval=15, blit=True)
        plt.show()
        return anim

if __name__ == "__main__":
    RaceSimulation().run()