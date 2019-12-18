from pylab import *
import networkx as nx
    
for _ in range(10):
    g = nx.barabasi_albert_graph(300, 4)
    data = []
    for t in range(299):

        # targeting highest degree node
        i = max(dict(g.degree()).items(), key = lambda x:x[1])[0]

        g.remove_node(i)
        lcc = max(nx.connected_component_subgraphs(g), key=len)
        data.append(lcc.number_of_nodes())
    plot(data)
    
xlabel('Number of removed nodes')
ylabel('Size of largest connected component')
show()
