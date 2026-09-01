import numpy as np

from OOP.race.config.airplane_config import AirplaneConfig


class Airplane:
    # Molde del avión en coordenadas locales
    BODY = np.array([[-40, 20], [0, 0]])
    WING_TOP = np.array([[-20, 0], [0.3, 0]])
    WING_BOT = np.array([[-20, 0], [-0.3, 0]])
    TAIL_TOP = np.array([[-40, -30], [0.15, 0]])
    TAIL_BOT = np.array([[-40, -30], [-0.15, 0]])
    SHAPE = [BODY, WING_TOP, WING_BOT, TAIL_TOP, TAIL_BOT]

    def __init__(self, config: AirplaneConfig, t: np.ndarray):
        self.config = config
        self.t = t

        # Corrección para t=0 cuando n<1, evita inf
        t_safe = t.copy()
        if config.n < 1:
            t_safe[0] = t_safe[1]

        # Física - vectorizado
        self.x = config.a * t_safe**config.n
        self.y = np.full_like(t, config.altitude, dtype=float)
        self.v = config.n * config.a * t_safe**(config.n - 1)

        # Estela punteada: cada 20 frames se guarda la posición
        # Optimización: en lugar de 3 for loops, usamos slicing
        self.dot_x = np.zeros_like(self.x)
        step = 20
        self.dot_x[0:step] = 0
        for i in range(step, len(t), step):
            self.dot_x[i:i+step] = self.x[i]

    def create_artists(self, ax):
        self.trail, = ax.plot([], [], f'{self.config.color}:o', ms=4, lw=2, alpha=0.6)
        self.parts = [ax.plot([], [], 'k', lw=lw)[0] for lw in [3,2,2,1,1]]
        return self.parts + [self.trail]

    def update_artists(self, frame: int):
        # El truco del broadcasting: shape (5,2,2) + [x,y]
        pos = np.array([self.x[frame], self.y[frame]])
        for part, offset in zip(self.parts, self.SHAPE):
            # offset es [[x1,x2],[y1,y2]] -> le sumamos pos
            xs = offset[0] + pos[0]
            ys = offset[1] + pos[1]
            part.set_data(xs, ys)

        self.trail.set_data(self.dot_x[:frame], self.y[:frame])