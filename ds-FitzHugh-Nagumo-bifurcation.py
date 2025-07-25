from pylab import *

a, b, c = 0.7, 0.8, 3.

Dt = 0.01

def initialize():
    global x, xresult, y, yresult
    x = y = 1.
    xresult = [x]
    yresult = [y]
    
def observe():
    global x, xresult, y, yresult
    xresult.append(x)
    yresult.append(y)

def update():
    global x, xresult, y, yresult
    nextx = x + c * (x - x**3 / 3 + y + z) * Dt
    nexty = y - (x - a + b * y) / c * Dt
    x, y = nextx, nexty

def plot_phase_space():
    initialize()
    for t in range(10000):
        update()
        observe()
    plot(xresult, yresult)
    axis('image')
    axis([-3, 3, -3, 3])
    title('z = ' + str(z))

zs = [-2, -1.5, -1., -0.5, 0]
for i in range(len(zs)):
    subplot(1, len(zs), i + 1)
    z = zs[i]
    plot_phase_space()

tight_layout()
show()
