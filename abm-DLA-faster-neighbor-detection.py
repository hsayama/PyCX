import pycxsimulator
from pylab import *

width = 200
height = 200
populationSize = 5000

noiseLevel = 1
collisionDistance = 2
CDsquared = collisionDistance ** 2

kw = int(width / collisionDistance) + 1
kh = int(height / collisionDistance) + 1

toBeRemoved = -1

def bin(a):
    return int(floor(a[0] / collisionDistance)), int(floor(a[1] / collisionDistance))

def initialize():
    global time, free, fixed, map

    time = 0
    
    free = []
    for i in range(populationSize - 1):
        free.append([uniform(0, width), uniform(0, height)])

    fixed = []
    fixed.append([width / 2, height / 2])

    map = [[[] for i in range(kh)] for j in range(kw)]
    for a in fixed:
        i, j = bin(a)
        map[i][j].append(a)

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
    global time, free, fixed, map

    time += 1

    # simulate random motion
    for ag in free:
        ag[0] += normal(0, noiseLevel)
        ag[1] += normal(0, noiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    # detect collision and change state
    for i in range(len(free)):
        ii, jj = bin(free[i])
        nbs = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= ii+di < kw and 0 <= jj+dj < kh:
                    nbs.extend(map[ii+di][jj+dj])
        for nb in nbs:
            if (free[i][0]-nb[0])**2 + (free[i][1]-nb[1])**2 < CDsquared:
                fixed.append(free[i])
                map[ii][jj].append(free[i])
                free[i] = toBeRemoved
                break

    # remove "toBeRemoved" free particles
    while toBeRemoved in free:
        free.remove(toBeRemoved)

pycxsimulator.GUI().start(func=[initialize, observe, update])
