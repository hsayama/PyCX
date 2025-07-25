import pycxsimulator
from pylab import *

import networkx as nx

n = 30 # number of nodes
k = 2  # number of inputs of each node

def initialize():
    global g
    g = nx.DiGraph()
    for i in range(n):
        for j in choice(range(n), k, replace = False):
            g.add_edge(j, i)
        g.nodes[i]['state'] = 1 if random() < .5 else 0
        lookuptable = choice([0, 1], 2**k)
        g.nodes[i]['rule'] = lambda nbs:lookuptable[int("".join(str(x) for x in nbs), 2)]    
    g.pos = nx.kamada_kawai_layout(g)

def observe():
    global g
    cla()
    nx.draw(g, vmin = 0, vmax = 1, pos = g.pos, node_color = [g.nodes[i]['state'] for i in g.nodes])

def update():
    global g
    for i in g.nodes:
        nbs = [g.nodes[j]['state'] for j in g.predecessors(i)]
        g.nodes[i]['nextstate'] = g.nodes[i]['rule'](nbs)
    for i in g.nodes:
        g.nodes[i]['state'] = g.nodes[i]['nextstate']

pycxsimulator.GUI().start(func=[initialize, observe, update])
