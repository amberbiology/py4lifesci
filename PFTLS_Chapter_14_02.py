#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 14

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

from numpy.random import exponential, uniform, seed
import matplotlib.pyplot as plt

# Model 2: toggle switch: four reactions

scaling = 1.0

alpha = 1     # synthesis mRNA
p = 10        # number of protein molecules per mRNA event
protein_degr_rate = 1/50.0   # degrading mRNA

w_fold  = 200      # Dissociation constant, and fold repression
K_D = 25      # strength of the DNA binding creating repression

def calculate_reaction_rates(n_A, n_B):

    A_conc = n_A/scaling
    B_conc = n_B/scaling
    
    A_synthesis_rate = scaling*alpha*(1+(B_conc/K_D/2)/w_fold*(2+(B_conc/K_D/2)))/(1+(B_conc/K_D/2))**2  # reaction 0
    B_synthesis_rate = scaling*alpha*(1+(A_conc/K_D/2)/w_fold*(2+(A_conc/K_D/2)))/(1+(A_conc/K_D/2))**2  # reaction 1
    A_degradation_rate    = scaling*protein_degr_rate*A_conc # reaction 2
    B_degradation_rate    = scaling*protein_degr_rate*B_conc # reaction 3

    return [A_synthesis_rate, B_synthesis_rate, A_degradation_rate, B_degradation_rate]

def do_reaction(n_A, n_B, next_reaction):

    if next_reaction == 0:
        n_A = n_A + p  # A are created     
    elif next_reaction == 1:
        n_B = n_B + p  # B are created
    elif next_reaction == 2:
        n_A -= 1       # A is degraded
    elif next_reaction == 3:
        n_B -= 1       # B is degraded

    return n_A, n_B

max_time = 10000.0

time_points = []
A_counts  = []
B_counts  = []

n_A = round(11*scaling)
n_B = round(34*scaling)

seed(50)
t = 0.0

num_reactions = 4

while t <= max_time:

    time_points.append(t)
    A_counts.append(n_A)
    B_counts.append(n_B)

    rates = calculate_reaction_rates(n_A, n_B)
    total_rates = sum(rates)

    delta_t = exponential(1.0/total_rates)
    type = uniform()*total_rates

    # find the reaction
    for reaction in range(0, num_reactions):
        if (sum(rates[0:reaction+1]) >= type):
            next_reaction=reaction
            break

    n_A, n_B = do_reaction(n_A, n_B, next_reaction) # carry out reaction

    t = t + delta_t 

fig1 = plt.figure()
plt.xlim(0, max_time)
plt.ylim(0, max(max(A_counts, B_counts)))
plt.xlabel('time')
plt.ylabel('# species')
plt.plot(time_points, A_counts, label="A") # species A
plt.plot(time_points, B_counts, label="B") # species B
plt.legend()
plt.show()


# Local variables:
# indent-tabs-mode: nil
# tab-width: 2
# py-indent-tabs-mode: nil
# End:
