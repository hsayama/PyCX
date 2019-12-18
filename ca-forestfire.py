import pycxsimulator
from pylab import *

width = 100
height = 100
initProb = 0.4
empty, tree, fire, char = range(4)

def initialize():
    global time, config, nextConfig

    time = 0

    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            if random() < initProb:
                state = tree
            else:
                state = empty
            config[y, x] = state

    height_half = int(height / 2) # added by toshi
    width_half  = int(width / 2)  # added by toshi
    config[height_half, width_half] = fire

    nextConfig = zeros([height, width])

def observe():
    cla()
    imshow(config, vmin = 0, vmax = 3, cmap = cm.binary)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == fire:
                state = char
            elif state == tree:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == fire:
                            state = fire
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

pycxsimulator.GUI().start(func=[initialize, observe, update])
