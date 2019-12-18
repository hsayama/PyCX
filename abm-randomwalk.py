import pycxsimulator
from pylab import *

populationSize = 100
noiseLevel = 1

def initialize():
    global time, agents

    time = 0

    agents = []
    for i in range(populationSize):
        newAgent = [normal(0, 1), normal(0, 1)]
        agents.append(newAgent)

def observe():
    cla()
    x = [ag[0] for ag in agents]
    y = [ag[1] for ag in agents]
    plot(x, y, 'bo', alpha = 0.2)
    axis('scaled')
    axis([-100, 100, -100, 100])
    title('t = ' + str(time))

def update():
    global time, agents

    time += 1

    for ag in agents:
        ag[0] += normal(0, noiseLevel)
        ag[1] += normal(0, noiseLevel)

pycxsimulator.GUI().start(func=[initialize, observe, update])
