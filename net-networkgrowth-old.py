import pycxsimulator
from pylab import *

import networkx as nx

m = 2

def initialize():
    global time, network, maxNodeID, positions

    time = 0

    network = nx.Graph()
    network.add_node(0)

    maxNodeID = 0

    positions = nx.random_layout(network)

def observe():
    cla()
    nx.draw(network, pos = positions)
    axis('image')
    title('t = ' + str(time))

def roulette(options, weights):
    weightsum = float(sum(weights))
    if weightsum == 0.0:
        weightsum = 1.0
    probabilities = [x / weightsum for x in weights]
    r = random()
    s = 0.0
    for k in range(len(options)):
        s += probabilities[k]
        if r <= s:
            break
    return options[k]

def update():
    global time, network, maxNodeID, positions

    time += 1

    degs = dict(network.degree())
    targets = list(degs.keys()) # fixed by toshi
    preferences = [d for d in degs.values()] # fixed by toshi
    # the first "d" could be varied to, e.g., 1, 1/d, d**2, etc.

    maxNodeID += 1
    network.add_node(maxNodeID)
    positions[maxNodeID] = array([normal(0, 0.1), normal(0, 0.1)])

    for i in range(m):
        target = roulette(targets, preferences)
        network.add_edge(maxNodeID, target)

    positions = nx.spring_layout(network, pos = positions, iterations = 2)

pycxsimulator.GUI().start(func=[initialize, observe, update])
