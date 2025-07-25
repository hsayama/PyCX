import pycxsimulator
from pylab import *

import networkx as nx

m = 2  # number of edges per new node

def initialize():
    global g
    g = nx.complete_graph(m)
    g.pos = nx.spring_layout(g)
    
def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos)

def update():
    global g

    n = g.number_of_nodes()
    degs = dict(g.degree())
    nds = list(degs.keys())
    weights = list(degs.values())
    s = float(sum(weights))
    weights = [w / s for w in weights] if s > 0 else [1. / n for i in range(n)]
    targets = choice(nds, size = m, p = weights, replace = False)

    newcomer = max(nds) + 1
    for j in targets:
        g.add_edge(newcomer, j)
    g.pos[newcomer] = (normal(0, 0.1), normal(0, 0.1))

    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 2)

pycxsimulator.GUI().start(func=[initialize, observe, update])
