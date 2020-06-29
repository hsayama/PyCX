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
        network.nodes[nd]['state'] = functioning
        network.nodes[nd]['load'] = random() * maxInitialLoad
    network.nodes[choice(list(network.nodes))]['load'] = 2.0 * capacity
    
    positions = nx.circular_layout(network)

def observe():
    cla()
    nx.draw(network, with_labels = False, pos = positions,
            cmap = cm.jet, vmin = 0, vmax = capacity,
            node_color = [network.nodes[nd]['load'] for nd in network.nodes])
    axis('image')
    title('t = ' + str(time))

def update():
    global time, network

    time += 1

    node_IDs = list(network.nodes)
    shuffle(node_IDs)
    for nd in node_IDs:
        if network.nodes[nd]['state'] == functioning:
            ld = network.nodes[nd]['load']
            if ld > capacity:
                network.nodes[nd]['state'] = failed
                nbs = [nb for nb in network.neighbors(nd) if network.nodes[nb]['state'] == functioning]
                if len(nbs) > 0:
                    loadDistributed = ld / len(nbs)
                    for nb in nbs:
                        network.nodes[nb]['load'] += loadDistributed

pycxsimulator.GUI().start(func=[initialize, observe, update])
