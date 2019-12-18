from pylab import *

def initialize():
    global x, result
    x = 0.1
    result = [x]

def observe():
    global x, result
    result.append(x)

def f(x):
    return x + r - x**2

def update():
    global x, result
    x = f(x)

def plot_phase_space():
    initialize()
    for t in range(100):
        update()
        observe()
    xmin = 0
    xmax = 2
    plot([xmin, xmax], [xmin, xmax], 'k')

    rng = linspace(xmin, xmax, 101)
    plot(rng, [f(x) for x in rng], 'k')

    horizontal = [result[0]]
    vertical = [result[0]] 
    for x in result:
        horizontal.append(vertical[-1])
        vertical.append(x)
        horizontal.append(x)
        vertical.append(x)    
    plot(horizontal, vertical, 'b')
    axis('image')
    axis([0, 2, 0, 2])
    title('r = ' + str(r))

rs = [0.1, 0.5, 1.0, 1.1, 1.5, 1.6]
for i in range(len(rs)):
    subplot(2, 3, i + 1)
    r = rs[i]
    plot_phase_space()

tight_layout()
show()
