import pycxsimulator
from pylab import *

import networkx as nx

n = 30 # number of nodes
k = 2  # number of inputs of each node

def initialize():
    global g, ph

    g = nx.DiGraph()
    for i in range(n):
        for j in choice(range(n), k, replace = False):
            g.add_edge(j, i)
        g.nodes[i]['state'] = 1 if random() < .5 else 0
        lookuptable = choice(range(2), 2**k)
        g.nodes[i]['rule'] = lambda nbs:lookuptable[int("".join(str(x) for x in nbs), 2)]    
    g.pos = nx.kamada_kawai_layout(g)

    ph = nx.DiGraph()
    ph.add_node(tuple(g.nodes[i]['state'] for i in g.nodes))
    ph.pos = nx.spring_layout(ph)
    ph.count = 0
    
def observe():
    global g, ph
    subplot(1, 2, 1)
    cla()
    nx.draw(g, vmin = 0, vmax = 1, pos = g.pos, node_color = [g.nodes[i]['state'] for i in g.nodes])
    title('Network state')
    axis('image')
    subplot(1, 2, 2)
    cla()
    nx.draw(ph, pos = ph.pos, node_size = 10)
    title('Phase space')
    axis('image')
    tight_layout()

def update():
    global g, ph
    
    s1 = tuple(g.nodes[i]['state'] for i in g.nodes)
    for i in g.nodes:
        nbs = [g.nodes[j]['state'] for j in g.predecessors(i)]
        g.nodes[i]['nextstate'] = g.nodes[i]['rule'](nbs)
    for i in g.nodes:
        g.nodes[i]['state'] = g.nodes[i]['nextstate']
    s2 = tuple(g.nodes[i]['state'] for i in g.nodes)

    if s2 in ph.nodes:
        ph.add_edge(s1, s2)
        ph.count += 1
        if ph.count > 20:
            # re-initialization of network state
            ph.count = 0
            for i in range(n):
                g.nodes[i]['state'] = 1 if random() < .5 else 0
            s2 = tuple(g.nodes[i]['state'] for i in g.nodes)
            ph.add_node(s2)
            ph.pos[s2] = array([0, 0])
    else:
        ph.add_edge(s1, s2)    
        
    ph.pos = nx.spring_layout(ph, pos = ph.pos, iterations = 2)

pycxsimulator.GUI().start(func=[initialize, observe, update])
