import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g, nextg
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['theta'] = random()
    nextg = g.copy()
    nextg.pos = g.pos
    
def observe():
    global g, nextg
    subplot(1, 2, 1)
    cla()
    nx.draw(g, cmap = cm.hsv, vmin = -1, vmax = 1,
            node_color = [sin(g.nodes[i]['theta']) for i in g.nodes],
            pos = g.pos)
    axis('image')

    subplot(1, 2, 2)
    cla()
    plot([cos(g.nodes[i]['theta']) for i in g.nodes],
         [sin(g.nodes[i]['theta']) for i in g.nodes], '.')
    axis('image')
    axis([-1.1, 1.1, -1.1, 1.1])

alpha = 2 # coupling strength
beta  = 1 # acceleration rate
Dt = 0.001 # Delta t

def update():
    global g, nextg
    for i in g.nodes:
        theta_i = g.nodes[i]['theta']
        nextg.nodes[i]['theta'] = theta_i + (beta * theta_i + alpha * \
            sum([g.nodes[j]['theta'] - theta_i for j in g.neighbors(i)]) \
            ) * Dt
    g, nextg = nextg, g

pycxsimulator.GUI().start(func=[initialize, observe, update])
