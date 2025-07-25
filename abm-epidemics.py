import pycxsimulator
from pylab import *

n = 1000            # number of agents
v = 0.01            # speed of agent movement
f = 0.01            # repulsion force constant
r = 0.02            # perception range
k = int(1 / r) + 1  # number of bins in each spatial dimension

p_inf = 0.5         # infection probability
p_rec = 0.05        # recovery probability

class agent:
    def __init__(self):
        self.x = rand(2)
        self.v = rand(2) - array([0.5, 0.5])
        self.v *= v / norm(self.v)
        self.s = 0
    def move(self):
        self.x += self.v
        if self.x[0] < 0: self.x[0] = 0; self.v[0] *= -1
        if self.x[1] < 0: self.x[1] = 0; self.v[1] *= -1
        if self.x[0] > 1: self.x[0] = 1; self.v[0] *= -1
        if self.x[1] > 1: self.x[1] = 1; self.v[1] *= -1

def initialize():
    global agents, Scount, Icount, Rcount
    agents = [agent() for i in range(n)]
    agents[0].s = 1
    Scount = [n - 1]
    Icount = [1]
    Rcount = [0]

def observe():
    global agents, Scount, Icount, Rcount
    subplot(1, 2, 1)
    cla()
    scatter([a.x[0] for a in agents], [a.x[1] for a in agents], c = [{0: 'c', 1: 'r', 2: 'g'}[a.s] for a in agents])
    axis('image')
    axis([0, 1, 0, 1])
    subplot(1, 2, 2)
    cla()
    plot(Scount, label = 'Susceptible')
    plot(Icount, label = 'Infected')
    plot(Rcount, label = 'Recovered')
    legend()
    tight_layout()

def bin(a):
    return int(floor(a.x[0] / r)), int(floor(a.x[1] / r))

def update():
    global agents, Scount, Icount, Rcount
    
    map = [[[] for i in range(k)] for j in range(k)]
    for a in agents:
        i, j = bin(a)
        map[i][j].append(a)
    
    for a in agents:
        i, j = bin(a)
        nbs = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= i+di < k and 0 <= j+dj < k:
                    nbs.extend(map[i+di][j+dj])
        
        a.a = array([0., 0.])
        a.ns = a.s
        for b in nbs:
            if a != b:
                d = norm(a.x - b.x)
                if d < r:
                    a.a += f * (a.x - b.x) / d
                    if a.s == 0 and b.s == 1:
                        if random() < p_inf:
                            a.ns = 1

    for a in agents:
        a.v += a.a
        a.v *= v / norm(a.v)
        a.move()
        if a.s == 1:
            if random() < p_rec:
                a.s = 2
        else:
            a.s = a.ns

    Scount.append(len([a for a in agents if a.s == 0]))
    Icount.append(len([a for a in agents if a.s == 1]))
    Rcount.append(len([a for a in agents if a.s == 2]))

pycxsimulator.GUI().start(func=[initialize, observe, update])
