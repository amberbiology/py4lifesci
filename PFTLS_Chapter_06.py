#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 6

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

import re

restrictionEnzymes = {}
restrictionEnzymes['bamH1'] = ['ggatcc',0]
restrictionEnzymes['sma1'] = ['cccggg',2]
restrictionEnzymes['nci1'] = ['cc[cg]gg',2]
restrictionEnzymes['scrF1'] = ['cc[atcg]gg',2]

sequence1 = 'atatatccgggatatatcccggatatat'
print(re.findall(restrictionEnzymes['bamH1'][0],sequence1))
print(re.findall(restrictionEnzymes['nci1'][0],sequence1))
print(re.findall(restrictionEnzymes['scrF1'][0],sequence1))


restrictionEnzymes['scrF1'] = ['cc.gg',2]
print(re.findall(restrictionEnzymes['scrF1'][0],sequence1))


promoter = 'ttgaca...................tataat'
promoter = 'ttgaca.{15,25}tataat'
sequence2 = 'cccccttgacaccccccccccccccccctataatccccc'
sequence3 = 'cccccttgacaccccccccccccccccccccctataatccccc'
print(re.findall(promoter,sequence2))
print(re.findall(promoter,sequence3))

print(re.finditer(promoter,sequence2))
matches = re.finditer(promoter,sequence2)
for m in matches:
    print(m.group())
    print(m.start(),m.end())


# Generating a randomized 250 million base chromosome may take a
# few minutes depending upon your computer's speed, so be patient.
# Searching it will be much (much) quicker :-)
import random
bases = ['a','t','c','g']
sequenceList = []
for n in range(0,250000000):
    sequenceList.append(random.choice(bases))
chromosome = ''.join(sequenceList)


import time
searchPattern = 'tataat'
t1 = time.time()
result = re.finditer(searchPattern,chromosome)
t2 = time.time()
print('Start time =',t1,'seconds. End time =',t2,' seconds.')


nsearch = 1000000
t1 = time.time()
for n in range(0,nsearch):
    result = re.finditer(searchPattern,chromosome)
t2 = time.time()
print('Average search time was ',(t2-t1)/float(nsearch),' seconds')
nmatches = 0

for match in result:
    nmatches += 1
print('Number of search hits = ',nmatches)


searchPattern = 'tat.at'
nsearch = 1000000
t1 = time.time()
for n in range(0,nsearch):
    result = re.finditer(searchPattern,chromosome)
t2 = time.time()
print('Average search time was ',(t2-t1)/float(nsearch),' seconds')
nmatches = 0

for match in result:
    nmatches += 1
print('Number of search hits = ',nmatches)
