import pycxsimulator
from pylab import *

import networkx as nx

n = 500
r = 3

def initialize():
    global g, aspl, acc
    g = nx.empty_graph(n)
    for i in g.nodes:
        for j in range(-r, r+1):
            if j != 0:
                g.add_edge(i, (i+j)%n)
    aspl = [nx.average_shortest_path_length(g)]
    acc = [nx.average_clustering(g)]
            
def observe():
    subplot(1, 3, 1)
    cla()
    nx.draw_circular(g, node_size = 0)
    axis('image')
    subplot(1, 3, 2)
    cla()
    plot(aspl)
    xlabel('# of rewiring')
    ylabel('Average shortest path length')
    subplot(1, 3, 3)
    cla()
    plot(acc)
    xlabel('# of rewiring')
    ylabel('Average clustering coefficient')
    tight_layout()

def update():
    global g, aspl, acc
    i = choice(g.nodes)
    j = choice(list(g.neighbors(i)))
    g.remove_edge(i, j)
    while True:
        j = choice(g.nodes)
        if j != i and not g.has_edge(i, j):
            break
    g.add_edge(i, j)
    
    aspl.append(nx.average_shortest_path_length(g))
    acc.append(nx.average_clustering(g))
    
pycxsimulator.GUI().start(func=[initialize, observe, update])
