from config.constants import OFFSETS

class AirplaneModel:
    def __init__(self, ax1):
        self.ax1 = ax1
        self.body = ax1.plot([],[],'k', linewidth=2)[0]
        self.right_wing = ax1.plot([],[],'k', linewidth=2)[0]
        self.left_wing = ax1.plot([],[],'k', linewidth=2)[0]
        self.right_tail = ax1.plot([],[],'k', linewidth=2)[0]
        self.left_tail = ax1.plot([],[],'k', linewidth=2)[0]
        self.parts = {
            'body': self.body,
            'right_wing': self.right_wing,
            'left_wing': self.left_wing,
            'right_tail': self.right_tail,
            'left_tail': self.left_tail
        }
    def update_coords(self, x, y):
        for name, part in self.parts.items():
            dx1, dx2, dy1, dy2 = OFFSETS[name]
            part.set_data([x+dx1, x+dx2], [y+dy1, y+dy2])