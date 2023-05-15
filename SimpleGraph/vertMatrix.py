import networkx as nx
import matplotlib.pyplot as plt

#define adjacency matrix
matrix = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1],
          [0, 0, 1, 1, 1]]

#define vertices
vertices = ["A", "B", "C", "D", "E"]

#create empty graph
G = nx.Graph()
G.add_nodes_from(vertices)

#iterate over the columns of the adjacency matrix
for i in range(len(matrix[0])):
    #find pairs of nodes connected by an edge in the current column
    edges = [(vertices[j], vertices[k]) for j in range(len(matrix)) for k in range(j, len(matrix)) if matrix[j][i] == 1 and matrix[k][i] == 1 and j != k]
    #add edges to the graph
    G.add_edges_from(edges)

#generate layout for the graph
pos = nx.spring_layout(G)

#draw graph with node labels
nx.draw(G, pos, with_labels=True)

#get edge labels
edge_labels = nx.get_edge_attributes(G, "weight")

#draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

#display graph
plt.show()