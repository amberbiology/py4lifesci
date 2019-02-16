#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 4

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

def biomarker(pDisease,pPosDisease,pPosNoDisease):
    pNoDisease = 1.0 - pDisease
    pPos = pPosDisease * pDisease + pPosNoDisease * pNoDisease
    return (pPosDisease * pDisease) / pPos

def bayes(outComeA,outComeB,pB,pAGivenB,pAGivenNotB):
    pNotB = 1.0 - pB
    pA = pAGivenB * pB + pAGivenNotB * pNotB
    pBGivenA = (pAGivenB * pB) / pA
    return 'p (%s | %s) = %.2f' % (outcomeB, outcomeA, pBGivenA)


pDisease = 0.015
pPosDisease = 0.8
pPosNoDisease = 0.04
print('Probability (disease | positive result) = ',biomarker(pDisease,pPosDisease,pPosNoDisease))

outcomeA = 'positive test result'
outcomeB = 'has disease'
pB = 0.015
pAGivenB = 0.8
pAGivenNotB = 0.04
print(bayes(outcomeA,outcomeB,pB,pAGivenB,pAGivenNotB))

geneName = 'TP53 tumor protein p53 [ Homo sapiens (human) ]'
geneID = 7157
matchProbability = 98.64756341
print('The gene to be analyzed is: %s' % geneName)
print('The gene ID number is: %d' % geneID)
print('The gene match probability is: %.3f' % matchProbability)
print('The results for geneId: %d: %s' % (geneID,geneName))
