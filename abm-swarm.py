import pycxsimulator
from pylab import *

class agent:
    def __init__(self):
        self.x = rand(2)
        self.v = rand(2) - array([0.5, 0.5])
        self.xs = [self.x[0]]
        self.ys = [self.x[1]]
    def accelerate(self):
        c = mean([a.x for a in agents])
        f = 0.5 * (c - self.x) / norm(c - self.x) 
        self.v += f # accelerating toward the center of mass
    def move(self):
        self.x += self.v
        self.xs.append(self.x[0])
        self.ys.append(self.x[1])
        if len(self.xs) > 10:
            del self.xs[0]
            del self.ys[0]
        
def initialize():
    global agents
    agents = [agent() for _ in range(50)]
    
def observe():
    cla()
    for a in agents:
        plot([a.x[0]], [a.x[1]], 'g.') # drawing current position
        plot(a.xs, a.ys, 'b', alpha = 0.1) # drawing trajectory as well
    axis('scaled')

def update():
    global agents
    for a in agents:
        a.accelerate()
    for a in agents:
        a.move()
        
pycxsimulator.GUI().start(func=[initialize, observe, update])
