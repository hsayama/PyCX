from pylab import *

import networkx as nx

### creating networks

# manual construction
g = nx.Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_node(5)
g.remove_node(4)
g.remove_edge(1, 2)

# complete graph with 10 nodes
K10 = nx.complete_graph(10)

# from adjacency matrix
mat = nx.from_numpy_matrix(array([[0,1,0,1,1],
                                  [1,0,0,1,0],
                                  [0,0,0,0,1],
                                  [1,1,0,0,0],
                                  [1,0,1,0,0]]))

### visualizing networks

subplot(1, 3, 1)
nx.draw(g)
axis('image')
title('g')

subplot(1, 3, 2)
nx.draw_circular(K10)
axis('image')
title('K10')

subplot(1, 3, 3)
nx.draw_random(mat)
axis('image')
title('mat')

show()

### obtaining basic information about networks

print('Number of nodes in K10 is', K10.number_of_nodes())

print('List of nodes in K10:')
print(K10.nodes)

print('Number of edges in K10 is', K10.number_of_edges())

print('List of edges in K10:')
print(K10.edges)

print("")

print('Adjacency matrix of K10 in numpy array format:')
print(nx.to_numpy_matrix(K10))

print("")

# connected components
cc = list(nx.connected_components(g)) # fixed by toshi
print('There are', len(cc), 'connected components in g')
print('They are:')
print(cc)

print("")

# shortest paths and characteristic path lengths
print('Shortest path from 1 to 4 in mat is:')
print(nx.shortest_path(mat, 1, 4))
print('whose length is', nx.shortest_path_length(mat, 1, 4))
print('Diameter (maximum of shortest path lengths) of mat is', nx.diameter(mat))
print('Average shortest path length of mat is', nx.average_shortest_path_length(mat))

print("")

# clustering coefficients
print('Clustering coefficients of nodes in mat are:')
print(nx.clustering(mat))
print('whose average is', nx.average_clustering(mat))

print("")

# degrees and degree distribution
print('Neighbors of node 0 in mat is:')
print(list(mat.neighbors(0)))
print('Its degree is', mat.degree(0))

print("")

print('Degrees of all nodes in mat are:')
print(dict(mat.degree()))

hist = nx.degree_histogram(mat)
print('When binned:')
print(hist)
print('See figure for its histogram')

plot(hist)
xlabel('Degree (k)')
ylabel('# of nodes (P(k))')
title("Degree distribution of the network 'mat'")

show()

print("")

# centralities
print('Betweenness centralities of all nodes in mat are:')
print(nx.betweenness_centrality(mat))
print('Closeness centralities of all nodes in mat are:')
print(nx.closeness_centrality(mat))
print('Eigenvector centralities of all nodes in mat are:')
print(nx.eigenvector_centrality(mat))
