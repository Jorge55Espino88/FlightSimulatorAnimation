from config.data import generate_flight_data
from managers.graph_manager import GraphManager

data = generate_flight_data(a=5, n=1.5)
gm = GraphManager()
gm.plot_data(data)
gm.show()