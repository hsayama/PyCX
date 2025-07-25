import pycxsimulator
from pylab import *

n = 100     # size of grid: n * n
Dh = 1. / n # spatial resolution, assuming space is [0,1] * [0,1]
Dt = 0.001   # temporal resolution

Du = 1e-5
Dv = 1e-5
eps = 0.2
q = 1.0e-3
f = 1

xvalues, yvalues = meshgrid(arange(0, 1, Dh), arange(0, 1, Dh))

def initialize():
    global u, v, nextu, nextv
    # initial configuration
    u = zeros([n, n])
    v = zeros([n, n])
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            u[x,y] = 1 if 0 < 8 * (xvalues[x,y] - 0.5) < yvalues[x,y] - 0.5 else 0
            v[x,y] = 1 if -(yvalues[x,y] - 0.5) < 8 * (xvalues[x,y] - 0.5) < 0 else 0
    nextu = zeros([n, n])
    nextv = zeros([n, n])
    
def observe():
    global u, v, nextu, nextv
    subplot(1, 2, 1)
    cla()
    imshow(u, vmin = 0, vmax = 1)
    title("u")
    subplot(1, 2, 2)
    cla()
    imshow(v, vmin = 0, vmax = 1)
    title("v")
    tight_layout()

def update():
    global u, v, nextu, nextv
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            # state-transition function
            uC, uR, uL, uU, uD = u[x,y], u[(x+1)%n,y], u[(x-1)%n,y], \
                                 u[x,(y+1)%n], u[x,(y-1)%n]
            vC, vR, vL, vU, vD = v[x,y], v[(x+1)%n,y], v[(x-1)%n,y], \
                                 v[x,(y+1)%n], v[x,(y-1)%n]
            uLapNum = (uR + uL + uU + uD - 4 * uC) / (Dh**2)
            vLapNum = (vR + vL + vU + vD - 4 * vC) / (Dh**2)
            nextu[x,y] = uC + (uC*(1-uC) - f*vC*(uC-q)/(uC+q) + Du*uLapNum) * Dt/eps
            nextv[x,y] = vC + (uC - vC + Dv * vLapNum) * Dt

    u, nextu = nextu, u
    v, nextv = nextv, v

pycxsimulator.GUI(stepSize = 50).start(func=[initialize, observe, update])

'''
initialize()
t = 0
observe()
savefig(str(t) + '.png')
for t in range(1, 100001):
    update()
    if t % 1000 == 0:
        print(t)
        observe()
        savefig(str(t) + '.png')
'''
