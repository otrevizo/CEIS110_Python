"""Example of preparing a graph using graphics libraries"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()
# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Add edges
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5),
                  (3, 6), (4, 6), (4, 7), (5, 6), (5, 8), (6, 7), (6, 8),
                  (6, 9), (7, 9), (8, 9)])
# Draw the graph
nx.draw(G, with_labels=True)
# Show the graph

plt.show()
