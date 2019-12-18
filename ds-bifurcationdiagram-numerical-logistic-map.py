from pylab import *

def initialize():
    global x, result
    x = 0.1
    result = []

def observe():
    global x, result
    result.append(x)

def update():
    global x, result
    x = r * x * (1 - x)

def plot_asymptotic_states():
    initialize()
    for t in range(100): # first 100 steps are discarded
        update()
    for t in range(100): # second 100 steps are collected
        update()
        observe()
    plot([r] * 100, result, 'b.', alpha = 0.3)

for r in arange(0, 4, 0.01):
    plot_asymptotic_states()

xlabel('r')
ylabel('x')
show()
