from pylab import *

def initialize():
    global x, result
    x = 0.1
    result = [x]

def observe():
    global x, result
    result.append(x)

def update():
    global x, result
    x =  r * x * (1 - x)

r = 4.0
initialize()
for t in range(100):
    update()
    observe()
plot(result)
title('r = ' + str(r))
show()
