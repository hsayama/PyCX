import pycxsimulator
from pylab import *

import networkx as nx

populationSize = 500
linkProbability = 0.01
initialInfectedRatio = 0.01
infectionProb = 0.2
recoveryProb = 0.5

susceptible = 0
infected = 1

def initialize():
    global time, network, positions, nextNetwork

    time = 0
    
    network = nx.erdos_renyi_graph(populationSize, linkProbability)

    positions = nx.random_layout(network)

    for i in network.nodes:
        if random() < initialInfectedRatio:
            network.nodes[i]['state'] = infected
        else:
            network.nodes[i]['state'] = susceptible

    nextNetwork = network.copy()

def observe():
    cla()
    nx.draw(network,
            pos = positions,
            node_color = [network.nodes[i]['state'] for i in network.nodes],
            cmap = cm.Wistia,
            vmin = 0,
            vmax = 1)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, network, nextNetwork

    time += 1

    for i in network.nodes:
        if network.nodes[i]['state'] == susceptible:
            nextNetwork.nodes[i]['state'] = susceptible
            for j in network.neighbors(i):
                if network.nodes[j]['state'] == infected:
                    if random() < infectionProb:
                        nextNetwork.nodes[i]['state'] = infected
                        break
        else:
            if random() < recoveryProb:
                nextNetwork.nodes[i]['state'] = susceptible
            else:
                nextNetwork.nodes[i]['state'] = infected

    network, nextNetwork = nextNetwork, network

pycxsimulator.GUI().start(func=[initialize, observe, update])
