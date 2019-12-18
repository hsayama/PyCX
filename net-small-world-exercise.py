import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g
    g = nx.convert_node_labels_to_integers(nx.grid_2d_graph(10, 10))
    g.pos = nx.spring_layout(g, k = 0.1)
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
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 3, k = 0.1)

pycxsimulator.GUI().start(func=[initialize, observe, update])
