#!/usr/bin/env python3

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

from numpy.random import exponential, uniform
import matplotlib.pyplot as plt

# Model 1: dimerization: just two reactions

# A + B -> AB  (k_D)
# AB -> A + B  (k_U)

k_D = 2.0
k_U = 1.0

time_points = []
A_counts  = []
B_counts  = []
AB_counts = []

t = 0.0
max_time = 10.0

# maximum number of molecules 
max_molecules = 100

n_A = max_molecules
n_B = max_molecules
n_AB = 0

# start loop
while t < max_time:

    A_counts.append(n_A)
    AB_counts.append(n_AB)
    time_points.append(t)

    dimer = k_D * n_A * n_B
    disso = k_U * n_AB
    total_rates = dimer + disso
    delta_t = exponential(1.0/total_rates)     # get time for next reaction
    type = uniform()*total_rates

    if type < dimer:  # do dimerization
        n_AB += 1
        n_A -= 1
        n_B -= 1
    else:             # do dissociation
        n_AB -= 1
        n_A  += 1
        n_B  += 1

    t = t + delta_t

fig1 = plt.figure()
plt.xlim(0, max_time)
plt.ylim(0, max_molecules)
plt.xlabel('time')
plt.ylabel('# species')

plt.plot(time_points, A_counts,  label="A")    # A monomer
plt.plot(time_points, AB_counts, label="AB")  # AB dimer
plt.legend()
plt.show()


# Local variables:
# indent-tabs-mode: nil
# tab-width: 2
# py-indent-tabs-mode: nil
# End:
