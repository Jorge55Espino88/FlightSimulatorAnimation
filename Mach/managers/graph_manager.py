import matplotlib.pyplot as plt

class GraphManager:
    # handles only drawing; performs no calculations
    # OOP principle: single responsibility

    def __init__(self):
        # 2 figures: one for V(t) and one for M(t)
        self.fig_v, self.ax_v = plt.subplots()
        self.fig_m, self.ax_m = plt.subplots()

    def plot_data(self, flight_data):
        # flight_data comes from generate_flight_data() -> dict with 3 altitudes

        for h, data in flight_data.items():
            t = data['t']
            V = data['V']
            M = data['M']

            # Graph 1: Speed vs Time
            self.ax_v.plot(t, V, label=f'h={h}m')

            # Graph 2: Mach vs. Time
            # This shows the difference based on altitude
            # At the same V, higher h -> higher M
            self.ax_m.plot(t, M, label=f'h={h}m c={data['c']:.1f} m/s')

        # Decorate V graph
        self.ax_v.set_xlabel('t [s]')
        self.ax_v.set_ylabel('V [m/s]')
        self.ax_v.legend()
        self.ax_v.set_title('Speed vs Time')

        # Decorate M graph
        self.ax_m.set_xlabel('t [s]')
        self.ax_m.set_ylabel('Mach [-]')
        self.ax_m.legend()
        self.ax_m.set_title('Mach vs Time - ISA Effect')
        self.ax_m.axhline(y=1.0, color='r', linestyle='--', label='Sonic barrier')
        # Red line at M=1 to see if any plane goes supersonic

    def show(self):
        plt.show()
