import networkx as nx
import matplotlib.pyplot as plt

#define the adjacency matrix
adj_matrix = [[0, 1, 1, 0, 1],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [1, 0, 0, 1, 0]]

#define the labels for the nodes
labels = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

#create an undirected graph
G = nx.Graph()

#iterate over the adjacency matrix
for i in range(len(adj_matrix)):
    for j in range(i, len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            #add an edge between nodes with a value of 1 in the adjacency matrix
            G.add_edge(labels[i], labels[j])

#draw the graph with node labels
nx.draw(G, with_labels=True)

#display graph
plt.show()

#create directed graph
G = nx.DiGraph()

#iterate over the adjacency matrix
for i in range(len(adj_matrix)):
    for j in range(i, len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            if labels[i] < labels[j]:
                #add an edge from the smaller labeled node to the larger labeled node
                G.add_edge(labels[i], labels[j])
            else:
                #add an edge from the larger labeled node to the smaller labeled node
                G.add_edge(labels[j], labels[i])

#draw directed graph with node labels
nx.draw(G, with_labels=True)

# Display the graph
plt.show()