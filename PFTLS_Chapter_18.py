#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 18

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

from random import shuffle
from numpy.random import random
import matplotlib.pyplot as plt

class Patient():
    # default state is susceptible
    def __init__(self, state = 'susceptible'): self.state = state
    def infect(self): self.state = 'infected'
    def recover(self):
        self.state = 'recovered'
        if False:                  # set to true to explore alternative model
            if random() < 0.8:
                self.state = 'susceptible'

class PatientList():
    # create lists for each type of agents 
    def __init__(self):
        self.susceptible_agents = []
        self.infected_agents = []
        self.recovered_agents = []

    def append(self, agent):
        if agent.state == 'susceptible': self.susceptible_agents.append(agent) 
        elif agent.state == 'infected': self.infected_agents.append(agent)
        elif agent.state == 'recovered': self.recovered_agents.append(agent)
        else: print "error: must be one of the three valid states"

    def infect(self):
        shuffle(self.susceptible_agents)   # shuffle list to get in random order
        patient = self.susceptible_agents.pop() # get patient and remove from list
        patient.infect()
        self.append(patient)  # internal method will handle appropriate list

    def recover(self):
        shuffle(self.infected_agents)    
        patient = self.infected_agents.pop()  
        patient.recover()
        self.append(patient)  

    def get_num_susceptible(self): return len(self.susceptible_agents)
    
    def get_num_infected(self): return len(self.infected_agents)

    def get_num_recovered(self): return len(self.recovered_agents)

    def get_num_total(self): return len(self.susceptible_agents)+len(self.infected_agents)+len(self.recovered_agents)

beta = 0.09  # susceptibility rate
gamma = 0.05 # recovery rate
susceptible_count = 1000
infected_count = 1
recovered_count = 0

# lists to record output
S = []
I = []
R = []
t = []
time = 0.0
patients = PatientList()

# create the individuals patients
for indiv in xrange(susceptible_count):
    agent = Patient()      # by default all new patients are susceptible
    patients.append(agent) # add to list

for indiv in xrange(infected_count):
    agent = Patient(state='infected')
    patients.append(agent)

for indiv in xrange(recovered_count):
    agent = Patient(state='recovered')
    patients.append(agent)

while patients.get_num_infected() > 0:

    for susc in xrange(patients.get_num_susceptible()):
        if random() < beta * (patients.get_num_infected() / float(patients.get_num_total())):
            patients.infect()  # infect patient

    for infected in xrange(patients.get_num_infected()):
        if random() < gamma:
            patients.recover() # recover patient

    # print "after update:", time, patients.num_susceptible, patients.num_infected, patients.num_recovered, num_total
    # record values for plotting
    t.append(time)
    S.append(patients.get_num_susceptible())
    I.append(patients.get_num_infected())
    R.append(patients.get_num_recovered())

    # update time
    time += 1

# plot output
fig1 = plt.figure()
plt.xlim(0, max(t))
plt.ylim(0, susceptible_count+infected_count+recovered_count)
plt.xlabel('time')
plt.ylabel('# patients')

plt.plot(t, S,  label="S")
plt.plot(t, I,  label="I")
plt.plot(t, R,  label="R")    
plt.legend()
plt.show()

# Local variables:
# indent-tabs-mode: nil
# tab-width: 2
# py-indent-tabs-mode: nil
# End:
