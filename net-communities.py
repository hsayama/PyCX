from pylab import *
import networkx as nx

g = nx.Graph()

imin, imax = 0, 9
for i in range(30):
    a, b = choice(range(imin, imax + 1), 2, replace = False)
    g.add_edge(a, b)

imin, imax = 10, 24
for i in range(40):
    a, b = choice(range(imin, imax + 1), 2, replace = False)
    g.add_edge(a, b)

imin, imax = 25, 49
for i in range(50):
    a, b = choice(range(imin, imax + 1), 2, replace = False)
    g.add_edge(a, b)

imin, imax = 0, 49
for i in range(10):
    a, b = choice(range(imin, imax + 1), 2, replace = False)
    g.add_edge(a, b)

nx.draw(g, pos = nx.kamada_kawai_layout(g))
show()
