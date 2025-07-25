"""
Author Name: Dheeraj Tommandru
E-mail: dtomman1@binghamton.edu/dheerajtls1234@gmail.com
Description:
This is implementation of Rob Axtell's and Joshua Epstein's basic Sugarscape Model.

Slightly updated by Hiroki Sayama
"""

import pycxsimulator
from pylab import *
from itertools import product
import random
from scipy.stats import multivariate_normal
from scipy.stats import randint as rd

distancing_ratio = 0.
x_lim, y_lim = 50, 50
num_agents = 150

class agent:
    pass

def initialize():
    global sugar, agents, wealth, deathcount, available_positions, sugar_positions, wealth,acount

    agents = [agent() for i in range(num_agents)]
    sugar = []
    a,b = arange(x_lim), arange(y_lim)
    available_positions = set(product(a, b))
    # assign genetic properties and initial positions to agents
    for ag in agents:
        element = random.randrange(0, len(available_positions))
        ap = {i:key for i, key in enumerate(available_positions)}
        available_positions.discard(ap[element])
        ag.x, ag.y  = ap[element]
        ag.metabolism = random.randint(1, 5)
        ag.sugar = random.randint(50, 100)
        ag.vision = random.randint(1, 4)
        ag.life = rd.rvs(50, 100, size=1)[0]
        ag.age = 0
        ap = None

    sugar_positions = {}

    for x in range(x_lim):
        for y in range(y_lim):
            sugar.append(agent())
            sugar[-1].x, sugar[-1].y = x, y
            sugar_positions[(x,y)] = len(sugar) - 1
            sugar[-1].max_capacity = random.randint(2, 10)
            sugar[-1].growth_rate = random.randint(1, 5)
            if x <= 24 and y <= 24:
                rv = multivariate_normal([12, 12], [[24, 0], [0, 24]])
                sugar[-1].available_sugar =int(round(rv.pdf([x, y])*100000, 0))
                sugar[-1].max_capacity = sugar[-1].available_sugar + 40
            elif x > 24 and y <= 24:
                sugar[-1].available_sugar = rd.rvs(0, 5, size=1)[0]
                sugar[-1].max_capacity = sugar[-1].available_sugar + 40
            elif x <= 24 and y > 24: 
                sugar[-1].available_sugar = rd.rvs(0, 4, size=1)[0]
                sugar[-1].max_capacity = sugar[-1].available_sugar + 40
            else:
                rv = multivariate_normal([37, 37], [[24, 0], [0, 24]])
                sugar[-1].available_sugar =int(round(rv.pdf([x,y]) * 100000, 0))
                sugar[-1].max_capacity = sugar[-1].available_sugar + 40

    wealth = [a.sugar for a in agents]
    deathcount = [0]
    acount = [len(agents)]

def observe():
    global sugar, agents, wealth, deathcount, available_positions, wealth, sugar_positions, acount
    subplot(2, 2, 1)
    cla()
    scatter([a.x for a in agents], [a.y for a in agents],c = [a.sugar for a in agents])
    axis('image')
    xlim([0, 49])
    ylim([0, 49])
    subplot(2, 2, 2)
    cla()
    scatter([s.x for s in sugar], [s.y for s in sugar], c = [s.available_sugar for s in sugar], alpha = 0.5)
    axis('image')
    subplot(2, 2, 3)
    cla()
    plot(deathcount, label = 'agents expired')
    xlabel("Time")
    ylabel("Number of agents")
    legend()
    subplot(2, 2, 4)
    cla()
    hist(wealth, label = 'wealth distribution')
    xlabel("Sugar")
    ylabel("Number of agents")
    legend()
    tight_layout()

def update():
    global sugar, agents, wealth, deathcount, available_positions, wealth, sugar_positions, acount
        
    dcount = 0
    for a in agents[:]:
        if (a.sugar < 0) or (a.age >= a.life):
            current_position = (a.x, a.y)
            agents.remove(a)
            new_agent = agent()
            new_agent.x, new_agent.y  = current_position
            new_agent.metabolism = random.randint(1, 5)
            new_agent.sugar = random.randint(50, 100)
            new_agent.vision = random.randint(1, 4)
            new_agent.life = rd.rvs(50, 100, size=1)[0]
            new_agent.age = 0
            agents.append(new_agent)
            dcount = dcount+1
        else:
            current_position = (a.x, a.y)
            neighbourhood_sugar_availability = {}
            neighbourhood_sugar_availability[current_position] = sugar[sugar_positions[(a.x, a.y)]].available_sugar                     
            for prospective_x in range(current_position[0] - a.vision, current_position[0] + a.vision + 1):
                for prospective_y in range(current_position[1] - a.vision, current_position[1] + a.vision + 1): 
                    if prospective_x > x_lim-1:
                        prospective_x = prospective_x - x_lim
                    if prospective_y > y_lim-1:
                        prospective_y = prospective_y - x_lim
                    if prospective_x < 0:
                        prospective_x = x_lim - prospective_x
                    if prospective_y < 0:
                        prospective_y = y_lim - prospective_y
                    if ((prospective_x, prospective_y) in available_positions) and ((prospective_x == current_position[0]) or (prospective_y == current_position[1])):
                            neighbourhood_sugar_availability[(prospective_x,prospective_y)] = sugar[sugar_positions[(prospective_x, prospective_y)]].available_sugar
            
            max_sugar_index = list(neighbourhood_sugar_availability.values()).index(max(list(neighbourhood_sugar_availability.values())))
            max_sugar_position = list(neighbourhood_sugar_availability.keys())[max_sugar_index]
            available_positions.discard(max_sugar_position)
            a.x, a.y = max_sugar_position
            available_positions.add(current_position)
            a.sugar = a.sugar - a.metabolism
            sugar[sugar_positions[max_sugar_position]].available_sugar = sugar[sugar_positions[max_sugar_position]].available_sugar - 10
            a.sugar = a.sugar + 10
            a.age = a.age + 1

    wealth = [a.sugar for a in agents]
    deathcount.append(dcount)
    acount.append(len(agents))

    for s in sugar:
        s.available_sugar = min(s.available_sugar + s.growth_rate, s.max_capacity)

pycxsimulator.GUI().start(func=[initialize, observe, update])
