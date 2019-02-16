#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 19

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

from numpy.random import binomial
from numpy import zeros
import matplotlib.pyplot as plt

# Python implementation of a Wright-Fisher model of evolution of one
# genetic locus with two alleles: A and B  includes version with:
# 1) just genetic drift 
# 2) genetic drift + overdominant selection

# selection on the heterozygote (AB) is bigger than either of the homozygotes
w_AA = 0.33
w_AB = 0.95
w_BB = 0.33

def do_selection(f_A, f_B):
    
    # calculate the current genotype frequencies from the allele frequencies
    f_AA = f_A**2
    f_AB = 2 * f_A * f_B
    f_BB = f_B**2 

    # now apply selection to get the absolute fitnesses of the genotypes
    # note these DO NOT sum to 1!
    g_AA = f_AA * w_AA
    g_AB = f_AB * w_AB
    g_BB = f_BB * w_BB

    # calculate the mean fitness, the weighted sum of the above
    w_bar = g_AA +  g_AB  + g_BB

    # now use mean fitness to get *new* genotype frequencies
    # note that these DO sum to 1!
    f_AA = g_AA / w_bar
    f_AB = g_AB / w_bar
    f_BB = g_BB / w_bar

    # get find new frequency of A:
    # AA genotype + half of all AB genotypes contain A
    # so add them together:
    f_A = f_AA + f_AB/2

    # frequency of B is just 1 - frequency of A
    # frequencies must sum to 1!
    f_B = 1 - f_A

    return f_A, f_B

def simulate_population(generations, num_alleles, selection=False):

    twoN = sum(num_alleles)   # calculate the total number of alleles (2N) by just summing total number of A and B alleles

    allele_counts = zeros((generations + 1, 2)) # create a 2xgeneration array of counts: A (col0) and B (col1), rows = generation
    allele_counts[0, :] = num_alleles           # initialize the allele counts at time, t=0

    for t in range(generations):

        # calculate allele frequencies
        f_A = allele_counts[t,0] / twoN                    # current frequency of A allele in the population
        f_B = (twoN - allele_counts[t,0]) / twoN           # current frequency of B allele in the population

        if selection:
            f_A, f_B = do_selection(f_A, f_B)

        allele_counts[t+1,0] = binomial(twoN, f_A)         # get new count for allele A, sampling from the binomial distribution with 2N trials and f_A
        allele_counts[t+1,1] = twoN - allele_counts[t+1,0] # get new count for allele B, by subtracting allele B count from total

        print(allele_counts[t+1, 0], allele_counts[t+1,1])

    return allele_counts

def plot_population(allele_counts, generations, selection):

    twoN = sum(num_alleles)   # calculate the total number of alleles (2N) by just summing total number of A and B alleles

    fig1 = plt.figure()
    plt.xlim(0, generations)
    plt.ylim(0, twoN)
    plt.xlabel('time')
    plt.ylabel('allele count')
    if selection:
        plt.title('drift+selection')
    else:
        plt.title('drift')
        
    time_points = list(range(generations + 1))
    plt.plot(time_points, allele_counts[:,0], label="A")  # A allele
    plt.plot(time_points, allele_counts[:,1], label="B")  # B allele
    plt.legend()
    plt.draw()

    return

if __name__ == "__main__":

    generations = 30          # generations
    num_alleles = [10, 10]    # initial number of alleles [A, B]

    print(num_alleles[0], num_alleles[1])

    # drift
    allele_counts = simulate_population(generations, num_alleles, selection=False)
    plot_population(allele_counts, generations, selection=False)

    # drift + selection
    allele_counts = simulate_population(generations, num_alleles, selection=True)
    plot_population(allele_counts, generations, selection=True)

    plt.show()

