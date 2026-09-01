class AirplaneManager:
    def __init__(self, ax, data):
        self.data = data
        self.body, = ax.plot([], [], 'k-', lw=2)
        self.top_wing, = ax.plot([], [], 'k-', lw=1.5)
        self.bot_wing, = ax.plot([], [], 'k-', lw=1.5)
        self.top_tail, = ax.plot([], [], 'k-', lw=1.5)
        self.bot_tail, = ax.plot([], [], 'k-', lw=1.5)
    def update(self, n):
        x = self.data.x_km[n]; y = self.data.y_km
        self.body.set_data([x-30, x], [y, y])
        self.top_wing.set_data([x-20, x-10], [y, y+0.25])
        self.bot_wing.set_data([x-20, x-10], [y, y-0.25])
        self.top_tail.set_data([x-30, x-25], [y, y+0.2])
        self.bot_tail.set_data([x-30, x-25], [y, y-0.2])
    def get(self): return [self.body, self.top_wing, self.bot_wing, self.top_tail, self.bot_tail]
