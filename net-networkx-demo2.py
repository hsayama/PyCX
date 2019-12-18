from pylab import *

import networkx as nx

### creating complex networks

er = nx.erdos_renyi_graph(200, 0.02)

ws = nx.watts_strogatz_graph(200, 4, 0.03)

ba = nx.barabasi_albert_graph(200, 4)

### visualizing networks

subplot(1, 3, 1)
nx.draw(er)
axis('image')
title('Erdos-Renyi')

subplot(1, 3, 2)
nx.draw(ws)
axis('image')
title('Watts-Strogatz')

subplot(1, 3, 3)
nx.draw(ba)
axis('image')
title('Barabasi-Albert')

show()

### obtaining degree distributions
print('Degrees of all nodes in ba are:')
print(dict(ba.degree))

# original degree distribution
hist = nx.degree_histogram(ba)
print('When binned:')
print(hist)

# complementary cummulative distribution function (CCDF)
ccdf = [sum(hist[k:]) for k in range(len(hist))]
print('Its CCDF:')
print(ccdf)

print('See figures for log-log plots')

subplot(1, 2, 1)
loglog(hist)
title('Original degree distribution')

subplot(1, 2, 2)
loglog(ccdf)
title('CCDF')

show()

### finding important structures

# minimum spanning tree
mst = nx.minimum_spanning_tree(ba)
nx.draw(mst)
title('Minimum spanning tree of ba')

# k-core
kc = nx.k_core(er)
print('Nodes in the k-core of er are:')
print(kc.nodes)
print('Size of the k-core: ', kc.number_of_nodes())

nx.draw(kc)
title('k-core of er')

show()
