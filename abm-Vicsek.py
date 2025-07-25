import pycxsimulator
from pylab import *

n = 500         # number of agents
v = 1           # speed of agent movement
r = 0.05        # perception range
r2 = r**2       # perception range squared
k = int(1 / r)  # number of bins in each spatial dimension 
Dt = 0.01       # time interval for updates 

eta = 0.1       # noise level

class agent:
    def __init__(self):
        self.x = rand(2)
        self.th = random() * 2 * pi
    def move(self):
        self.x += v * array([cos(self.th), sin(self.th)]) * Dt
        if self.x[0] < 0: self.x[0] += 1
        if self.x[1] < 0: self.x[1] += 1
        if self.x[0] >= 1: self.x[0] -= 1
        if self.x[1] >= 1: self.x[1] -= 1

def initialize():
    global agents
    agents = [agent() for i in range(n)]
    
def observe():
    global agents
    cla()
    plot([a.x[0] for a in agents], [a.x[1] for a in agents], 'bo')
    axis('image')
    axis([0, 1, 0, 1])

def bin(a):
    return int(floor(a.x[0] / r)), int(floor(a.x[1] / r))

def update():
    global agents

    map = [[[] for i in range(k)] for j in range(k)]
    for a in agents:
        i, j = bin(a)
        map[i][j].append(a)
        
    for a in agents:
        i, j = bin(a)
        nbs = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                nbs.extend(map[(i+di)%k][(j+dj)%k])
        for b in list(nbs):
            dx, dy = abs(a.x - b.x)
            if min(dx, 1 - dx)**2 + min(dy, 1 - dy)**2 >= r2:
                nbs.remove(b)
        av = mean([[cos(b.th), sin(b.th)] for b in nbs], axis = 0)
        a.nth = arctan2(av[1], av[0]) + uniform(- eta / 2, eta / 2)
        
    for a in agents:
        a.th = a.nth
        a.move()

pycxsimulator.GUI().start(func=[initialize, observe, update])
