import networkx as nx
import matplotlib.pyplot as plt

# 1. Create a simple graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
edge_list = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
H = nx.Graph(edge_list)

# 2. Draw the graph structure
nx.draw(H, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800)

# 3. Render and display the visual window
plt.show()