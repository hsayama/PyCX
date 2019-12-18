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

pycxsimulator.GUI().start(func=[initialize, observe, update])
