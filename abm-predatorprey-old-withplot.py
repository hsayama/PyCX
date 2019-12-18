import pycxsimulator
from pylab import *

width = 100
height = 100

initialRabbitPopulation = 100
rabbitReproductionRate = 0.1
rabbitPopulationLimit = 500
rabbitNoiseLevel = 2

initialFoxPopulation = 30
foxReproductionRate = 0.5
foxPopulationLimit = 500
foxNoiseLevel = 3
foxHungerLimit = 10

collisionDistance = 2
CDsquared = collisionDistance ** 2
toBeRemoved = -1

def initialize():
    global time, rabbits, foxes, rabbitData, foxData

    time = 0
    
    rabbits = []
    for i in range(initialRabbitPopulation):
        rabbits.append([uniform(0, width), uniform(0, height)])

    foxes = []
    for i in range(initialFoxPopulation):
        foxes.append([uniform(0, width), uniform(0, height), 0])

    rabbitData = [initialRabbitPopulation]
    foxData = [initialFoxPopulation]

def observe():
    subplot(1, 2, 1)
    cla()
    if rabbits != []:
        x = [ag[0] for ag in rabbits]
        y = [ag[1] for ag in rabbits]
        scatter(x, y, color = 'pink')
    if foxes != []:
        x = [ag[0] for ag in foxes]
        y = [ag[1] for ag in foxes]
        scatter(x, y, color = 'brown')
    axis('scaled')
    axis([0, width, 0, height])
    title('t = ' + str(time))

    subplot(1, 2, 2)
    cla()
    plot(rabbitData, color = 'pink')
    plot(foxData, color = 'brown')
    title('Populations')

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def update():
    global time, rabbits, foxes, rabbitData, foxData

    time += 1
    
    # simulate random motion
    for ag in rabbits:
        ag[0] += normal(0, rabbitNoiseLevel)
        ag[1] += normal(0, rabbitNoiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    for ag in foxes:
        ag[0] += normal(0, foxNoiseLevel)
        ag[1] += normal(0, foxNoiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    # detect collision and change state
    for i in range(len(foxes)):
        foxes[i][2] += 1                      # fox's hunger level increasing
        for j in range(len(rabbits)):
            if rabbits[j] != toBeRemoved:
                if (foxes[i][0]-rabbits[j][0])**2 + (foxes[i][1]-rabbits[j][1])**2 < CDsquared:
                    foxes[i][2] = 0           # fox ate rabbit and hunger level reset to 0
                    rabbits[j] = toBeRemoved  # rabbit eaten by fox
        if foxes[i][2] > foxHungerLimit:
            foxes[i] = toBeRemoved            # fox died due to hunger

    # remove "toBeRemoved" agents
    while toBeRemoved in rabbits:
        rabbits.remove(toBeRemoved)
    while toBeRemoved in foxes:
        foxes.remove(toBeRemoved)

    # count survivors' populations
    rabbitPopulation = len(rabbits)
    foxPopulation = len(foxes)

    # produce offspring
    for i in range(len(rabbits)):
        if random() < rabbitReproductionRate * (1.0 - float(rabbitPopulation) / float(rabbitPopulationLimit)):
            rabbits.append(rabbits[i][:]) # making and adding a copy of the parent
    for i in range(len(foxes)):
        if foxes[i][2] == 0 and random() < foxReproductionRate * (1.0 - float(foxPopulation) / float(foxPopulationLimit)):
            foxes.append(foxes[i][:]) # making and adding a copy of the parent

    rabbitData.append(len(rabbits))
    foxData.append(len(foxes))

pycxsimulator.GUI().start(func=[initialize, observe, update])
