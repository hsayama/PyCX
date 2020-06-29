import pycxsimulator
from pylab import *

import networkx as nx

populationSize = 2000
numberOfLinks = 5000
initialInfectedRatio = 0.01
maxTime = 200

susceptible = 0
infected = 1

er_network = 0
ba_network = 1

def networksimulation(networkType, infectionProb, recoveryProb):

    if networkType == er_network:
        linkProbability = float(numberOfLinks) / float(populationSize * (populationSize - 1) / 2)
        network = nx.erdos_renyi_graph(populationSize, linkProbability)
    else:
        network = nx.barabasi_albert_graph(populationSize, int(numberOfLinks / populationSize))

    for i in network.nodes:
        if random() < initialInfectedRatio:
            network.nodes[i]['state'] = infected
        else:
            network.nodes[i]['state'] = susceptible

    nextNetwork = network.copy()

    for time in range(maxTime):

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

    return [network.nodes[i]['state'] for i in network.nodes].count(infected)

infectionRates = arange(0, 0.3, 0.01)

result = []
print('Starting simulations on Erdos-Renyi networks...')
for i in infectionRates:
    print('Infection rate =', i)
    s = 0
    for k in range(5):
        s += networksimulation(er_network, i, 0.5)
    s /= 5.0
    result.append(s)
subplot(1, 2, 1)
plot(infectionRates, result)
title("Erdos-Renyi Network")

result = []
print('Starting simulations on Barabasi-Albert networks...')
for i in infectionRates:
    print('Infection rate =', i)
    s = 0
    for k in range(5):
        s += networksimulation(ba_network, i, 0.5)
    s /= 5.0
    result.append(s)
subplot(1, 2, 2)
plot(infectionRates, result)
title("Barabasi-Albert Network")

show()
