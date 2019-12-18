import pycxsimulator
from pylab import *

n = 1000 # number of particles
sd = 0.1 # standard deviation of Gaussian noise

def initialize():
    global xlist, ylist
    xlist = []
    ylist = []
    for i in range(n):
        xlist.append(normal(0, 1))
        ylist.append(normal(0, 1))
    
def observe():
    global xlist, ylist
    cla()
    plot(xlist, ylist, '.', alpha = 0.2)
    axis('image')
    axis([-20, 20, -20, 20])

def update():
    global xlist, ylist
    for i in range(n):
        xlist[i] += normal(0, sd)
        ylist[i] += normal(0, sd)

def num_particles (val = n):
    '''
    Number of particles.
    Make sure you change this parameter while the simulation is not running,
    and reset the simulation before running it. Otherwise it causes an error!
    '''
    global n
    n = int(val)
    return val

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [num_particles]).start(func=[initialize, observe, update])
