class TrailsManager:
    def __init__(self, ax, data):
        self.data = data
        self.h, = ax.plot([], [], 'r--', lw=1.5)
        self.v, = ax.plot([], [], 'k:', lw=1.5)
    def update(self, n):
        x = self.data.x_km[n]; y = self.data.y_km
        self.h.set_data([0, x], [y, y])
        self.v.set_data([x, x], [0, y])
    def get(self): return [self.h, self.v]