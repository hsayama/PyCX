from pylab import *
import networkx as nx

g = nx.karate_club_graph()

subplot(2, 3, 1)
nx.draw_spring(g)
axis('image')
title('spring layout')

subplot(2, 3, 2)
nx.draw_random(g)
axis('image')
title('random layout')

subplot(2, 3, 3)
nx.draw_circular(g)
axis('image')
title('circular layout')

subplot(2, 3, 4)
nx.draw_spectral(g)
axis('image')
title('spectral layout')

subplot(2, 3, 5)
shells = [[0, 1, 2, 32, 33],
          [3, 5, 6, 7, 8, 13, 23, 27, 29, 30, 31],
          [4, 9, 10, 11, 12, 14, 15, 16, 17, 18,
           19, 20, 21, 22, 24, 25, 26, 28]]
nx.draw_shell(g, nlist = shells)
axis('image')
title('shell layout')

subplot(2, 3, 6)
nx.draw_kamada_kawai(g)
axis('image')
title('Kamada-Kawai layout')

tight_layout()
show()
