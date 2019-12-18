import pycxsimulator
from pylab import *

# import necessary modules
# define model parameters

def initialize():
    global # list global variables
    # initialize system states
    
def observe():
    global # list global variables
    cla() # to clear the visualization space
    # visualize system states

def update():
    global # list global variables
    # update system states for one discrete time step

pycxsimulator.GUI().start(func=[initialize, observe, update])
