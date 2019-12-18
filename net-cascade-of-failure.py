import pycxsimulator
from pylab import *

import networkx as nx

functioning = 1
failed = 0

capacity = 1.0
maxInitialLoad = 0.6

def initialize():
    global time, network, positions

    time = 0

    network = nx.watts_strogatz_graph(200, 4, 0.02)
    for nd in network.nodes:
        network.node[nd]['state'] = functioning
        network.node[nd]['load'] = random() * maxInitialLoad
    network.node[choice(list(network.nodes))]['load'] = 2.0 * capacity
    
    positions = nx.circular_layout(network)

def observe():
    cla()
    nx.draw(network, with_labels = False, pos = positions,
            cmap = cm.jet, vmin = 0, vmax = capacity,
            node_color = [network.node[nd]['load'] for nd in network.nodes])
    axis('image')
    title('t = ' + str(time))

def update():
    global time, network

    time += 1

    node_IDs = list(network.nodes)
    shuffle(node_IDs)
    for nd in node_IDs:
        if network.node[nd]['state'] == functioning:
            ld = network.node[nd]['load']
            if ld > capacity:
                network.node[nd]['state'] = failed
                nbs = [nb for nb in network.neighbors(nd) if network.node[nb]['state'] == functioning]
                if len(nbs) > 0:
                    loadDistributed = ld / len(nbs)
                    for nb in nbs:
                        network.node[nb]['load'] += loadDistributed

pycxsimulator.GUI().start(func=[initialize, observe, update])
