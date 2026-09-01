class GraphManager:
    def __init__(self, ax, data, y_data, label):
        self.data = data; self.y_data = y_data
        self.line, = ax.plot(data.t, y_data, 'b-', lw=2, label=label)
        self.h, = ax.plot([], [], 'r:', marker='o')
        self.v, = ax.plot([], [], 'b:', marker='o')
        self.p, = ax.plot([], [], 'go', ms=8)
        ax.grid(True); ax.legend()
    def update(self, n):
        t = self.data.t[n]; y = self.y_data[n]
        self.h.set_data([0, t], [y, y])
        self.v.set_data([t, t], [0, y])
        self.p.set_data([t], [y])
    def get(self): return [self.line, self.h, self.v, self.p]