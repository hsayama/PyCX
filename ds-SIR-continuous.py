from pylab import *

a = 1.0 # infection rate
b = 0.2 # recovery rate

Dt = 0.001

def initialize():
    global S, I, t, Sdata, Idata, tdata
    S, I, t = 0.999, 0.001, 0.
    Sdata, Idata, tdata = [S], [I], [t]
    
def observe():
    global S, I, t, Sdata, Idata, tdata
    Sdata.append(S)
    Idata.append(I)
    tdata.append(t)

def update():
    global S, I, t, Sdata, Idata, tdata
    nextS = S + (- a * S * I) * Dt
    nextI = I + (a * S * I - b * I) * Dt
    S, I = nextS, nextI
    t = t + Dt

initialize()
while t < 50.:
    update()
    observe()

plot(tdata, Sdata, 'c', label = 'Susceptible')
plot(tdata, Idata, 'r', label = 'Infected')
legend()
show()
