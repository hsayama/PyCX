import pycxsimulator
from pylab import *

width = 50
height = 50
numberOfStates = 2
r = 1

def initialize():
    global time, config, nextConfig

    time = 0
    
    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            config[y, x] = randint(numberOfStates)

    nextConfig = zeros([height, width])

def observe():
    cla()
    imshow(config, vmin = 0, vmax = numberOfStates - 1, cmap = cm.winter)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            counts = [0] * numberOfStates
            for dx in range(- r, r + 1):
                for dy in range(- r, r + 1):
                    s = int(config[(y+dy)%height, (x+dx)%width])
                    counts[s] += 1
            maxCount = max(counts)
            maxStates = []
            for i in range(numberOfStates):
                if counts[i] == maxCount:
                    maxStates.append(i)
            state = choice(maxStates)
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

pycxsimulator.GUI().start(func=[initialize, observe, update])
