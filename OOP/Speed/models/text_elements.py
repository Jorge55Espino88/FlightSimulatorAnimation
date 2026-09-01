class TextElements:
    def __init__(self, ax1):
        self.clock_text = ax1.text(0.02, 0.96, "", transform=ax1.transAxes, fontsize=12, bbox=dict(facecolor="white", alpha=0.7))
        self.km_text = ax1.text(0.27, 0.09, "", transform=ax1.transAxes, fontsize=12, bbox=dict(facecolor="white", alpha=0.7))

    def update(self, data, num):
        self.clock_text.set_text(f"Time: {data.t[num]:.2f} hrs")
        self.km_text.set_text(f"Distance: {data.x_km[num]:.1f} km")