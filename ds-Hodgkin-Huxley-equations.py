from pylab import *

I = 10. # injected current

C = 1.
ENa = 115.
gNa = 120.
EK = -12.
gK = 36.
EL = 10.6
gL = 0.3

Dt = 0.01

def initialize():
    global V, Vdata, n, ndata, m, mdata, h, hdata, t, tdata
    V, n, m, h = 0., 0., 0., 0.
    Vdata = [V]
    ndata = [n]
    mdata = [m]
    hdata = [h]
    t = 0.
    tdata = [t]
    
def observe():
    global V, Vdata, n, ndata, m, mdata, h, hdata, t, tdata
    Vdata.append(V)
    ndata.append(n)
    mdata.append(m)
    hdata.append(h)
    tdata.append(t)

def an(V):
    return (0.1 - 0.01 * V) / (exp(1 - 0.1 * V) - 1)

def am(V):
    return (2.5 - 0.1 * V) / (exp(2.5 - 0.1 * V) - 1)

def ah(V):
    return 0.07 * exp(- V / 20.)

def bn(V):
    return 0.125 * exp(-V / 80.)

def bm(V):
    return 4. * exp(-V / 18.)

def bh(V):
    return 1. / (exp(3 - 0.1 * V) + 1)

def update():
    global V, Vdata, n, ndata, m, mdata, h, hdata, t, tdata
    nextV = V + (I - (gNa * (m**3) * h * (V - ENa) + gK * (n**4) * (V-EK) + gL * (V - EL))) / C * Dt
    nextn = n + (an(V) * (1 - n) - bn(V) * n) * Dt
    nextm = m + (am(V) * (1 - m) - bm(V) * m) * Dt
    nexth = h + (ah(V) * (1 - h) - bh(V) * h) * Dt
    V, n, m, h = nextV, nextn, nextm, nexth
    t = t + Dt

initialize()
while t < 100.:
    update()
    observe()

subplot(2, 1, 1)
plot(tdata, Vdata, label = 'V')
legend()

subplot(2, 1, 2)
plot(tdata, ndata, label = 'n')
plot(tdata, mdata, label = 'm')
plot(tdata, hdata, label = 'h')
legend()

tight_layout()
show()