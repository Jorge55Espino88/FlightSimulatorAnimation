class Trails:
    def __init__(self, ax1):
        self.horizontal_ax1 = ax1.plot([],[],'r--', linewidth=2)[0]
        self.vertical_ax1 = ax1.plot([],[],'k:', linewidth=2)[0]
        self.house_1 = ax1.plot([100,100],[0,1.0],'k',linewidth=7)[0]
        self.house_2 = ax1.plot([300,300],[0,1.0],'k',linewidth=7)[0]
        self.house_3 = ax1.plot([700,700],[0,0.7],'k',linewidth=15)[0]
        self.house_4 = ax1.plot([900,900],[0,0.9],'k',linewidth=18)[0]
        self.house_5 = ax1.plot([1300,1300],[0,1.0],'k',linewidth=20)[0]

    def update(self, data, num):
        self.vertical_ax1.set_data([data.x_km[num], data.x_km[num]], [0, data.y_km[num]])
        self.horizontal_ax1.set_data([data.x_km[0], data.x_km[num]], [data.y_km[0], data.y_km[0]])