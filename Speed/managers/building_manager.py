from matplotlib.patches import Rectangle


class BuildingManager:
    def __init__(self, ax):
        xs = [100, 300, 700, 900, 1300]
        hs = [1.07, 1.07, 0.85, 1.10, 1.20]
        self.buildings = []
        for x,h in zip(xs, hs):
            b = Rectangle((x,0), 20, h, color='black')
            ax.add_patch(b)
            self.buildings.append(b)
    def get(self): return self.buildings