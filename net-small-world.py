import pycxsimulator
from pylab import *

import networkx as nx

n = 30 # number of nodes
k = 4  # number of neighbors of each node

def initialize():
    global g
    g = nx.Graph()
    for i in range(n):
        for j in range(1, int(k/2) + 1):
            g.add_edge(i, (i + j) % n)
            g.add_edge(i, (i - j) % n)
    g.pos = nx.spring_layout(g)
    g.count = 0
    
def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos)

def update():
    global g
    g.count += 1
    if g.count % 20 == 0: # rewiring once in every 20 steps
        nds = list(g.nodes)
        i = choice(nds)
        if g.degree(i) > 0:
            g.remove_edge(i, choice(list(g.neighbors(i))))
            nds.remove(i)
            for j in g.neighbors(i):
                nds.remove(j)
            g.add_edge(i, choice(nds))

    # simulation of node movement
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 3)

pycxsimulator.GUI().start(func=[initialize, observe, update])
