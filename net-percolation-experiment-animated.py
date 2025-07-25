import pycxsimulator
from pylab import *

import networkx as nx

n = 1000

def initialize():
    global g, lcc
    g = nx.empty_graph(n)
    g.pos = nx.random_layout(g)
    lcc = [len(max(nx.connected_components(g), key = len))]
            
def observe():
    subplot(1, 2, 1)
    cla()
    nx.draw(g, g.pos, node_size = 1)
    axis('image')
    subplot(1, 2, 2)
    cla()
    plot(lcc)
    xlabel('# of edges added')
    ylabel('Size of LCC')
    tight_layout()

def update():
    global g, lcc
    i, j = choice(g.nodes, 2, replace = False)
    g.add_edge(i, j)
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 2)
    lcc.append(len(max(nx.connected_components(g), key = len)))
    
pycxsimulator.GUI().start(func=[initialize, observe, update])
