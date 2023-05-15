import networkx as nx
import matplotlib.pyplot as plt

#define graph as dictionary
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D', 'E'],
    'D': ['C', 'E'],
    'E': ['A', 'B', 'C', 'D']
}

#create graph object from dictionary
G = nx.Graph(graph)

#draw graph with node labels
nx.draw(G, with_labels=True)
plt.show()

#get list of nodes in graph
nodes = list(G.nodes())
print("Nodes: ", nodes)

#get list of edges in graph
edges = list(G.edges())
print("Edges: ", edges)

#find node with highest degree
max_degree = 0
max_degree_node = None
for node in G.nodes():
    degree = G.degree(node)
    if degree > max_degree:
        max_degree = degree
        max_degree_node = node

print("The vertex with the highest number of incident vertices: {max_degree_node}")
print("Neighborhood: ", list(G.neighbors(max_degree_node)))

#write graph to graphmL file
nx.write_graphml(G, "graph.graphml")

#read graph from graphmL file
H = nx.read_graphml("graph.graphml")

#create subplots to display original graph and read graph
plt.subplot(1, 2, 1)
nx.draw(G, with_labels=True)

plt.subplot(1, 2, 2)
nx.draw(H, with_labels=True)

plt.show()

#add new node to graph H
H.add_node("node1")

#draw modified graph H
nx.draw(H)
plt.show()