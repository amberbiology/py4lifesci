#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 16

# The text of the book is (c) Amber Biology LLC (www.amberbiology.com)
# The Python code from the book is released into the public domain, as follows:

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

from numpy import zeros
from numpy.random import random, seed
import matplotlib.pyplot as plt

def simulation_step(CA, next_CA):

    for x in range(width):
        for y in range(height):

            cell_state = CA[y, x]  # get current state

            activating_cells = 0
            inhibiting_cells = 0

            # count the number of inhibiting cells within the radius
            for xpos in range(- inhibitor_radius, inhibitor_radius + 1):
                for ypos in range(- inhibitor_radius, inhibitor_radius + 1):
                    inhibiting_cells += CA[(y+ypos)%height, (x+xpos)%width]

            # count the number of activating cells within the radius
            for xpos in range(- activator_radius, activator_radius + 1):
                for ypos in range(- activator_radius, activator_radius + 1):
                    activating_cells += CA[(y+ypos)%height, (x+xpos)%width]

            # if weighted sum of activating cells is greater than inhibiting cells in neighbourhood
            # we induce differentiation in the current cell 
            if (activating_cells * activator_weight) + (inhibiting_cells * inhibitor_weight) > 0:
                cell_state = 1
            else:
                cell_state = 0

            # now update the state
            next_CA[y, x] = cell_state

    return next_CA

seed()

probability_of_black = 0.5
width = 100
height = 100

# initialize cellular automata (CA)
CA = zeros([height, width])       # main CA
next_CA = zeros([height, width])  # CA next timestep

activator_radius = 1
activator_weight = 1
inhibitor_radius = 5
inhibitor_weight = -0.1

time = 0

# initialize the CA
for x in range(width):
    for y in range(height):
        if random() < probability_of_black:
            cell_state = 1
        else:
            cell_state = 0
        CA[y, x] = cell_state

# create plot
fig1 = plt.figure()

# loop through times
for time in range(10):
    plt.pcolor(CA, vmin = 0, vmax = 1, cmap = "copper_r")  # plot current CA
    plt.axis('image')
    plt.title('time: ' + str(time))
    plt.draw()
    plt.pause(0.5)

    CA = simulation_step(CA, next_CA)  # advance the simulation

