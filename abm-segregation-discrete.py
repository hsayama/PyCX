import pycxsimulator
from pylab import *

width = 50
height = 50
density = 0.8
threshold = 0.7

def initialize():
    global time, config, agents, empty

    agents = []
    empty = []

    time = 0
    
    config = zeros([height, width])
    for x in range(width):
        for y in range(height):
            if random() < density:
                agents.append((y, x))
                if random() < 0.5:
                    config[y, x] = 1
                else:
                    config[y, x] = -1
            else:
                empty.append((y, x))

def observe():
    cla()
    imshow(config, vmin = -1, vmax = 1, cmap = cm.bwr)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, agents, empty

    time += 1

    sequence = list(range(len(agents)))
    shuffle(sequence)
    for i in sequence:
        y, x = agents[i]
        state = config[y, x]
        similar = 0
        total = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not ((dx == 0) and (dy == 0)):
                    v = config[(y + dy) % height, (x+dx) % width]
                    if (v != 0):
                        total += 1
                    if (v == state):
                        similar += 1
        if (similar < threshold * total):
            j = randint(len(empty))
            new_y, new_x = empty[j]
            agents[i] = (new_y, new_x)
            config[new_y, new_x] = state
            empty[j] = (y, x)
            config[y, x] = 0

pycxsimulator.GUI().start(func=[initialize, observe, update])
