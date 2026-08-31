class TextManager:
    def __init__(self, ax):
        self.t1 = ax.text(0.05, 0.9, '', transform=ax.transAxes, bbox=dict(facecolor='white', alpha=0.8))
        self.t2 = ax.text(0.4, 0.15, '', transform=ax.transAxes, bbox=dict(facecolor='white', alpha=0.8))
    def update(self, data, n):
        self.t1.set_text(f'Time: {data.t[n]:.2f} hrs')
        self.t2.set_text(f'Distance: {data.x_km[n]:.1f} km')
    def get(self): return [self.t1, self.t2]