import matplotlib.pyplot as plt
import networkx as nx

# 1. Initialize as a Directed Graph
G = nx.DiGraph()

# 2. Add nodes
G.add_nodes_from(["A", "B", "C", "D"])

# 3. Define our edges
# We use an edge attribute "connection_type" to track the intent
directed_edges = [("A", "B"), ("B", "C")]
undirected_edges = [("C", "D"), ("D", "A")]

# Add directed edges
for u, v in directed_edges:
    G.add_edge(u, v, connection_type="directed")

# Add undirected edges as bidirectional pairs
for u, v in undirected_edges:
    G.add_edge(u, v, connection_type="undirected")
    G.add_edge(v, u, connection_type="undirected")

# 4. Separate edges for custom styling during visualization
pure_directed = [
    (u, v) for u, v, d in G.edges(data=True) if d["connection_type"] == "directed"
]
pure_undirected = [
    (u, v) for u, v, d in G.edges(data=True) if d["connection_type"] == "undirected"
]

# 5. Position nodes for drawing
pos = nx.spring_layout(G)

# Draw nodes and labels
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=200)
nx.draw_networkx_labels(G, pos)

# Draw directed edges (with arrows)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=pure_directed,
    edge_color="lightblue",
    arrows=True,
    arrowstyle="->",
    arrowsize=20,
)

# Draw undirected edges (hide arrows to simulate undirected behavior)
nx.draw_networkx_edges(
    G, pos, edgelist=pure_undirected, edge_color="black", arrows=False
)

plt.title("Mixed Network Graph")
plt.axis("off")
plt.show()
