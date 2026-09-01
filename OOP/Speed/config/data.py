import numpy as np

class Data:
    def __init__(self):
        self.t = np.arange(0.0, 2.0, 0.02) # 0 a 2 hrs,
        self.k = 800.0
        self.x_km = self.k * self.t # X = 800*t
        self.speed_x = np.full_like(self.t, self.k) # V = 800
        self.y_km = 2.0
        self.x_max = 1600.0
        self.y_max = 3.0