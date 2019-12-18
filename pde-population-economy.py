import pycxsimulator
from pylab import *

L = 5000.
k = 100.
n = int(L/k)
Dt = 0.1

def initialize():
    global P, P2, E, E2
    P = zeros([n, n])
    E = zeros([n, n])
    for x in range(n):
        for y in range(n):
            P[x,y] = 0.5 + uniform(-0.1, 0.1)
    P2 = zeros([n, n])
    E2 = zeros([n, n])
    
def observe():
    global P, E

    subplot(1, 2, 1)
    cla()
    imshow(P, vmin = 0, vmax = 1)
    title('Population')

    subplot(1, 2, 2)
    cla()
    imshow(E, vmin = 0, vmax = 5)
    title('Economy')
    
Dp, De, a, b, c = 1250, 250, 600, 1., 0.2
    
def update():
    global P, P2, E, E2
    for x in range(n):
        for y in range(n):
            Pc,Pr,Pl,Pt,Pb = P[x,y], P[(x+1)%n,y], P[(x-1)%n,y], P[x,(y+1)%n], P[x,(y-1)%n]
            Ec,Er,El,Et,Eb = E[x,y], E[(x+1)%n,y], E[(x-1)%n,y], E[x,(y+1)%n], E[x,(y-1)%n]
            lapP = (Pr+Pl+Pt+Pb-4*Pc) / (k**2)
            lapE = (Er+El+Et+Eb-4*Ec) / (k**2)
            P2[x, y] = Pc + (Dp*lapP - a*(Pc*lapE + (Pr-Pl)*(Er-El)/(4*k**2) + (Pt-Pb)*(Et-Eb)/(4*k**2))) * Dt
            E2[x, y] = Ec + (De*lapE + b*Pc - c*Ec) * Dt
    P, P2, E, E2 = P2, P, E2, E
    
pycxsimulator.GUI(stepSize = 50).start(func=[initialize, observe, update])
