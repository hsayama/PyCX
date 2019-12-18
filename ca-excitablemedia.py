import pycxsimulator
from pylab import *

width = 100
height = 100
initProb = 0.1
maxState = 6

def initialize():
    global time, config, nextConfig
    
    time = 0

    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            if random() < initProb:
                state = maxState
            else:
                state = 0
            config[y, x] = state

    nextConfig = zeros([height, width])

def observe():
    cla()
    imshow(config, vmin = 0, vmax = maxState, cmap = cm.binary)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == 0:
                num = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == maxState:
                            num += 1
                if random() * 3 < num:
                    state = maxState
                else:
                    state = 0
            else:
                state -= 1
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

pycxsimulator.GUI().start(func=[initialize, observe, update])
