import pycxsimulator
from pylab import *

import networkx as nx

def initialize():
    global g, loc
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['count'] = 0
    loc = 0
    g.nodes[loc]['count'] += 1
    
def observe():
    global g, loc
    cla()
    nx.draw(g, pos = g.pos, node_color = [g.nodes[i]['count'] for i in g.nodes], 
            cmap = cm.binary, edgecolors = 'k')
    nx.draw_networkx_nodes(g, pos = g.pos, nodelist = [loc], node_color = 'r')

def update():
    global g, loc
    loc = choice(list(g.neighbors(loc)))
    g.nodes[loc]['count'] += 1

pycxsimulator.GUI().start(func=[initialize, observe, update])
