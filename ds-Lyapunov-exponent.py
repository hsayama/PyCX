from pylab import *

def initialize():
    global x, result
    x = 0.1
    result = [logdFdx(x)]

def observe():
    global x, result
    result.append(logdFdx(x))

def update(r):
    global x, result
    x = x + r - x**2

def logdFdx(x):
    return log(abs(1 - 2*x))

def lyapunov_exponent(r):
    initialize()
    for t in range(100):
        update(r)
        observe()
    return mean(result)

rvalues = arange(0, 2, 0.01)
lambdas = [lyapunov_exponent(r) for r in rvalues]
plot(rvalues, lambdas)
plot([0, 2], [0, 0])

xlabel('r')
ylabel('Lyapunov exponent')
show()
