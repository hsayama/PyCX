import pycxsimulator
from pylab import *

width = 50
height = 50
initProb = 0.5

Ra = 1
Ri = 5
Wa = 1
Wi = 0.1

def initialize():
    global time, config, nextConfig

    time = 0
    
    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            if random() < initProb:
                state = 1
            else:
                state = 0
            config[y, x] = state

    nextConfig = zeros([height, width])

def observe():
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            na = ni = 0
            for dx in range(- Ra, Ra + 1):
                for dy in range(- Ra, Ra + 1):
                    na += config[(y+dy)%height, (x+dx)%width]
            for dx in range(- Ri, Ri + 1):
                for dy in range(- Ri, Ri + 1):
                    ni += config[(y+dy)%height, (x+dx)%width]
            if na * Wa - ni * Wi > 0:
                state = 1
            else:
                state = 0
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

pycxsimulator.GUI().start(func=[initialize, observe, update])
