#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 2

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

# Declaring numerical variables
h2oOxygens = 1
h2oHydrogens = 2
h2o_density_in_grams_per_liter = 1000
oxygenMass = 15.9994
hydrogenMass = 1.00794
avogadro = 6.023e23

# Declaring string variables
buffer = 'Tris'
buffer = "MES"
jfk = "I'm proud to say 'Ich bin ein berliner'"
carbonMass = "12.0107"

limerick = """ Said a young researcher named Spode
               Having reached the end of his road
               'I have far too much data
               For this hand calculator
               If only I knew how to code!' """

# Calculate mass of water molecule and output it to console
h2oMass = h2oOxygens * oxygenMass + h2oHydrogens * hydrogenMass
print 'Molecular weight of H20 = ',h2oMass

# A simple function to calculate molar volumes
def calculateMolarVolume(mass,density):
    volume = mass/density
    return volume

h2oMolarVolume = calculateMolarVolume(h2oMass,h2o_density_in_grams_per_liter)
print 'Volume of 1 mole of H2O = ',h2oMolarVolume,'L'

# A function to calculate molecules per liter
def moleculesPerLiter(mass,density):
    molarVolume = calculateMolarVolume(mass,density)
    numberOfMolarVolumes = 1.0/molarVolume
    numberOfMolecules = avogadro * numberOfMolarVolumes
    return numberOfMolecules

h2oMoleculesPerLiter = moleculesPerLiter(h2oMass,h2o_density_in_grams_per_liter)
print 'Number of molecules of H2O in 1L = ',h2oMoleculesPerLiter

# Beware the quirks of integer arithmetic!
a = 3
b = 6
print 'a/b = ',a/b
print 'b/a = ',b/a
print '12/5 = ',12/5
a = 3.0
b = 6.0
print 'a/b = ',a/b

# ... and don't forget mathematical operator precedence
a = 6.0
b = 3.0
c = 5.0
print 'a/b+c = ',a/b+c
print 'a/(b+c) = ',a/(b+c)

# Function for calculating buffer recipes that uses conditionals
def bufferRecipe(buffer,molarity):
    if buffer == 'Tris':
        grams = 121.14
    elif buffer == 'MES':
        grams = 217.22
    elif buffer == 'HEPES':
        grams = 238.30
    else:
        return 'Huh???'
    gramsPerLiter = grams * molarity
    return gramsPerLiter

# Examples of how Python conditionals work
something = 6
anotherThing = 6
if something == anotherThing:
    print 'This statement will be printed'
    print 'So will this one'
print 'This statement gets printed either way'

anotherThing = 4
if something == anotherThing:
    print 'This statement will be printed'
    print 'So will this one'
print 'This statement gets printed either way'

something = 10
if something == 6:
    print 'something is 6'
elif something == 4:
    print 'something is 4'
else:
    print 'something is something else entirely'

# Testing our bufferRecipe function
print 'Recipe for 0.1M Tris = ',bufferRecipe('Tris',0.1),'g/L'
print 'Recipe for 0.5M MES = ',bufferRecipe('MES',0.5),'g/L'
print 'Recipe for 1mM HEPES = ',bufferRecipe('HEPES',1.0e-3),'g/L'
print 'Recipe for 1.0M Goop = ',bufferRecipe('Goop',1.0),'g/L'
