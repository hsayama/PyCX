import pycxsimulator
from pylab import *

import networkx as nx

memorized_letters = [
    # Letter 'C'
    [-1, 1, 1, 1,
     1, -1, -1, -1,
     1, -1, -1, -1,
     -1, 1, 1, 1],
    # Letter 'P'
    [1, 1, 1, -1,
     1, -1, -1, 1,
     1, 1, 1, -1,
     1, -1, -1, -1]
]

def initialize():
    global g
    g = nx.complete_graph(4 * 4)
    g.pos = {}
    for x in range(4):
        for y in range(4):
            g.pos[y * 4 + x] = (x, -y)
    for i, j in g.edges:
        g.edges[i, j]['weight'] = sum([letter[i] * letter[j] for letter in memorized_letters])
    for i in g.nodes:
        g.nodes[i]['state'] = choice([-1, 1])
    
def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos, cmap = cm.winter, vmin = -1, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes])
    axis('image')
    
def update():
    global g
    i = choice(list(g.nodes))
    s = sum([g.edges[i, j]['weight'] * g.nodes[j]['state'] for j in g.neighbors(i)])
    g.nodes[i]['state'] = 1 if s > 0 else -1 if s < 0 else g.nodes[i]['state']

pycxsimulator.GUI().start(func=[initialize, observe, update])
