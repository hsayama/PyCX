from pylab import *
import networkx as nx

g = nx.Graph()

imin, imax = 0, 9
for i in range(30):
    g.add_edge(randint(imin, imax + 1),randint(imin, imax + 1))

imin, imax = 10, 24
for i in range(40):
    g.add_edge(randint(imin, imax + 1),randint(imin, imax + 1))

imin, imax = 25, 49
for i in range(50):
    g.add_edge(randint(imin, imax + 1),randint(imin, imax + 1))

imin, imax = 0, 49
for i in range(10):
    g.add_edge(randint(imin, imax + 1),randint(imin, imax + 1))

nx.draw(g, pos = nx.spring_layout(g, k = 0.07, iterations = 300))
show()
