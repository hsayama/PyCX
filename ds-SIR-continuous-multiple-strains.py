from pylab import *

a = [1.1, 1.2, 1.3] # infection rates
b = [0.5, 0.4, 0.3] # recovery rates
m = 0.00001         # mutation rate

Dt = 0.001

def initialize():
    global S, I, t, Sdata, Idata, tdata
    S, I, t = [0.999, 1., 1.], [0.001, 0., 0.], 0.
    Sdata, Idata, tdata = [S], [I], [t]
    
def observe():
    global S, I, t, Sdata, Idata, tdata
    Sdata.append(S)
    Idata.append(I)
    tdata.append(t)

def update():
    global S, I, t, Sdata, Idata, tdata
    nextS = [S[k] - a[k] * S[k] * I[k] * Dt for k in range(3)]
    nextI = [I[k] + (a[k] * S[k] * I[k] - b[k] * I[k] + (m * I[k-1] if k > 0 else 0) - (m * I[k] if k < 2 else 0)) * Dt for k in range(3)]
    S, I = nextS, nextI
    t = t + Dt

initialize()
while t < 50.:
    update()
    observe()

plot(tdata, mean(array(Sdata), axis = 1), 'c', label = 'Susceptible')
plot(tdata, array(Idata)[:, 0], 'r', label = 'Infected: Strain 1')
plot(tdata, array(Idata)[:, 1], 'm', label = 'Infected: Strain 2')
plot(tdata, array(Idata)[:, 2], 'g', label = 'Infected: Strain 3')
legend()
show()
