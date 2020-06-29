import pycxsimulator
from pylab import *

import networkx as nx

k = 4

def initialize():
    global g
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = choice(range(k))
    
def observe():
    global g
    cla()
    nx.draw(g, cmap = cm.rainbow, vmin = 0, vmax = k - 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

def update():
    global g
    listener = choice(list(g.nodes))
    nbs = list(g.neighbors(listener))
    if nbs != []:
        speaker = choice(nbs)
        g.nodes[listener]['state'] = g.nodes[speaker]['state']

pycxsimulator.GUI().start(func=[initialize, observe, update])
