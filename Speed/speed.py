import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from config.data import Data
from managers.building_manager import BuildingManager
from managers.air_manager import AirplaneManager
from managers.trail_manager import TrailsManager
from managers.text_manager import TextManager
from managers.graph_manager import GraphManager


data = Data()
fig = plt.figure(figsize=(11,6), dpi=100)
ax1 = plt.subplot2grid((2,2), (0,0), colspan=2)
ax2 = plt.subplot2grid((2,2), (1,0))
ax3 = plt.subplot2grid((2,2), (1,1))

ax1.set_xlim(0, data.x_max)
ax1.set_ylim(0, data.y_max)
ax1.set_title('Airplane')
ax1.grid(True)

ax2.set_xlim(0, 2.0)
ax2.set_ylim(0, 1600)
ax2.set_title('X distance vs time')
ax3.set_xlim(0, 2.0)
ax3.set_ylim(0, 1000)
ax3.set_title('Speed vs time')

bm = BuildingManager(ax1)
am = AirplaneManager(ax1, data)
tm = TrailsManager(ax1, data)
txm = TextManager(ax1)
g2 = GraphManager(ax2, data, data.x_km, 'X = 800*t^1')
g3 = GraphManager(ax3, data, data.speed_x, 'dX/dt = 800 km/hr')

plt.tight_layout()

def update(n):
    am.update(n)
    tm.update(n)
    txm.update(data, n)
    g2.update(n)
    g3.update(n)
    return bm.get() + am.get() + tm.get() + txm.get() + g2.get() + g3.get()

ani = FuncAnimation(fig, update, frames=len(data.t), interval=20, blit=True)
plt.show()