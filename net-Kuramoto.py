import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['theta'] = 2 * pi * random()
        g.nodes[i]['omega'] = 1. + uniform(-0.05, 0.05)
    nextg = g.copy()
    nextg.pos = g.pos
    
def observe():
    global g, nextg
    cla()
    nx.draw(g, cmap = cm.hsv, vmin = -1, vmax = 1,
            node_color = [sin(g.nodes[i]['theta']) for i in g.nodes],
            pos = g.pos)

alpha = 1 # coupling strength
Dt = 0.01 # Delta t

def update():
    global g, nextg
    for i in g.nodes:
        theta_i = g.nodes[i]['theta']
        nextg.nodes[i]['theta'] = theta_i + (g.nodes[i]['omega'] + alpha * ( \
            sum([sin(g.nodes[j]['theta'] - theta_i) for j in g.neighbors(i)]) \
            / g.degree(i))) * Dt
    g, nextg = nextg, g

pycxsimulator.GUI().start(func=[initialize, observe, update])
