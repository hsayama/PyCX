from pylab import *

s = 10.
r = 30.
b = 3.
Dt = 0.01

def initialize():
    global x, xresult, y, yresult, z, zresult, t, timesteps
    x = y = z = 1.
    xresult = [x]
    yresult = [y]
    zresult = [z]
    t = 0.
    timesteps = [t]
    
def observe():
    global x, xresult, y, yresult, z, zresult, t, timesteps
    xresult.append(x)
    yresult.append(y)
    zresult.append(z)
    timesteps.append(t)

def update():
    global x, xresult, y, yresult, z, zresult, t, timesteps
    nextx = x + (s * (y - x)) * Dt
    nexty = y + (r * x - y - x * z) * Dt
    nextz = z + (x * y - b * z) * Dt
    x, y, z = nextx, nexty, nextz
    t = t + Dt

initialize()
while t < 100.:
    update()
    observe()

sectionY = []
sectionZ = []
for i in range(len(xresult) - 1):
    x0 = xresult[i]
    x1 = xresult[i+1]
    if x0 * x1 < 0:
        sectionY.append((yresult[i] + yresult[i+1]) / 2)
        sectionZ.append((zresult[i] + zresult[i+1]) / 2)

plot(sectionY, sectionZ, 'bo', alpha = 0.5)
xlabel('y')
ylabel('z')
title('Poincare section at x = 0')
show()
