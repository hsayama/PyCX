import pycxsimulator
from pylab import *

width = 100
height = 100
populationSize = 1000

noiseLevel = 1
collisionDistance = 2
CDsquared = collisionDistance ** 2

toBeRemoved = -1

def initialize():
    global time, free, fixed

    time = 0
    
    free = []
    for i in range(populationSize - 1):
        free.append([uniform(0, width), uniform(0, height)])

    fixed = []
    fixed.append([width / 2, height / 2])

def observe():
    cla()
    if free != []:
        x = [ag[0] for ag in free]
        y = [ag[1] for ag in free]
        scatter(x, y, color = 'cyan')
    if fixed != []:
        x = [ag[0] for ag in fixed]
        y = [ag[1] for ag in fixed]
        scatter(x, y, color = 'blue')
    axis('scaled')
    axis([0, width, 0, height])
    title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def update():
    global time, free, fixed

    time += 1

    # simulate random motion
    for ag in free:
        ag[0] += normal(0, noiseLevel)
        ag[1] += normal(0, noiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    # detect collision and change state
    for i in range(len(free)):
        for j in range(len(fixed)):
            if (free[i][0]-fixed[j][0])**2 + (free[i][1]-fixed[j][1])**2 < CDsquared:
                fixed.append(free[i])
                free[i] = toBeRemoved
                break

    # remove "toBeRemoved" free particles
    while toBeRemoved in free:
        free.remove(toBeRemoved)

pycxsimulator.GUI().start(func=[initialize, observe, update])
