import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0
    nextg = g.copy()
    nextg.pos = g.pos
    
def observe():
    global g
    cla()
    nx.draw(g, cmap = cm.Wistia, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

p_i = 0.5 # infection probability
p_r = 0.5 # recovery probability

def update():
    global g, nextg
    for a in g.nodes:
        if g.nodes[a]['state'] == 0: # if susceptible
            nextg.nodes[a]['state'] = 0
            for b in g.neighbors(a):
                if g.nodes[b]['state'] == 1: # if neighbor b is infected
                    if random() < p_i:
                        nextg.nodes[a]['state'] = 1
        else: # if infected
            nextg.nodes[a]['state'] = 0 if random() < p_r else 1
    nextg, g = g, nextg

pycxsimulator.GUI().start(func=[initialize, observe, update])
