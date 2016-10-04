#!/usr/bin/env python

__author__ = 'Alex Lancaster'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 17

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

import numpy as np
import matplotlib
from matplotlib import pylab as plt
import matplotlib.animation as animation
matplotlib.use('TKAgg')

generations = 5000

# setup empty arrays
Fx = np.zeros(generations+1)
Ch = np.zeros(generations+1)

# initialize the population
Ch[0] = 100.0
Fx[0] = 10.0

# set the parameters
dt = 0.01      # scale parameters so that each timestep doesn't "jump"

b_Ch = 0.5     # prey birth rate   (br)
d_Ch = 0.015   # predation rate (death rate of prey)  (a)
b_Fx = 0.015       # predator birth rate    (c)
d_Fx = 0.5         # predator death rate  (d)

# run predator-prey!

for t in range(0, generations):
              # old prey   + newly born prey - killed prey 
    Ch[t+1] = Ch[t] + dt * (b_Ch * Ch[t]     - d_Ch * Fx[t] * Ch[t])    
              # old predators  - predator death    +  births of predators          
    Fx[t+1] = Fx[t]  + dt *   (-d_Fx * Fx[t]       +  b_Fx * Fx[t] * Ch[t])

# do the plotting

# get the maximum of the population so we can scale window properly
popMax = max(max(Fx), max(Ch))

fig1 = plt.figure()
plt.xlim(0, generations)
plt.ylim(0, popMax)
plt.xlabel('time')
plt.ylabel('population count')
    
time_points = range(generations + 1)
plt.plot(time_points, Fx, label="Foxes")  
plt.plot(time_points, Ch, label="Chickens")  
plt.legend()
plt.draw()

# create state space figure with animation

fig2 = plt.figure()

plt.plot(Ch, Fx, 'g-', alpha=0.2)  # state space
plt.xlabel('Chickens (prey population size)')
plt.ylabel('Foxes (predator population size)')
line, = plt.plot(Ch[0], Fx[0], 'r.', markersize=10) # draw point as red

def init():
  line.set_data([], [])  # set empty data
  return line,

def animate(i):
  line.set_xdata(Ch[i])
  line.set_ydata(Fx[i])
  return line,

ani = animation.FuncAnimation(fig2, animate, xrange(0, len(time_points)), init_func=init,
                              interval=25, blit=False)

plt.show()

# Local variables:
# indent-tabs-mode: nil
# tab-width: 2
# py-indent-tabs-mode: nil
# End:
