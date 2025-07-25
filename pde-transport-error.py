import pycxsimulator
from pylab import *

from mpl_toolkits.mplot3d import Axes3D

n = 100     # size of grid: n * n
Dh = 1. / n # spatial resolution, assuming space is [0,1] * [0,1]
Dt = 0.1   # temporal resolution

wx, wy = -0.01, 0.03 # constant velocity of movement

xvalues, yvalues = meshgrid(arange(0, 1, Dh), arange(0, 1, Dh))

def initialize():
    global config, nextconfig
    # initial configuration
    config = exp(-((xvalues - 0.5)**2 + (yvalues - 0.5)**2) / (0.2**2))
    nextconfig = zeros([n, n])
    
def observe():
    global config, nextconfig
    fig = gcf()
    ax = fig.add_subplot(111, projection='3d')
    ax.cla()
    ax.plot_surface(xvalues, yvalues, config, rstride = 5, cstride = 5)
    ax.grid(False)
    ax.set_zlim(0, 1)

def update():
    global config, nextconfig
    for x in range(n):
        for y in range(n):
            # state-transition function
            nextconfig[x, y] = config[x, y] - (  wx * config[(x+1)%n, y]
                                               - wx * config[(x-1)%n, y]
                                               + wy * config[x, (y+1)%n]
                                               - wy * config[x, (y-1)%n])\
            * Dt/(2*Dh)

    config, nextconfig = nextconfig, config

pycxsimulator.GUI(stepSize = 50).start(func=[initialize, observe, update])
