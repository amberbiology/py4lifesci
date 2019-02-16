#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 3

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

mySequence = 'atcg'
print('Sequence length is ',len(mySequence))


for c in mySequence:
    print(c)

for c in mySequence:
    print('This line will be executed for each pass through the loop')
    print('So will this one')
print('This line will only be executed at the end')


i = 0
for c in mySequence:
    i += 1
    print(i,c)


print(mySequence[0])
print(mySequence[3])
print(mySequence[-1])
print(mySequence[0:4])
print(mySequence[:4])
print(mySequence[2:3])
print(mySequence[2:4])
print(mySequence[2:])
print(mySequence[-3:])


mySequenceAsAList = ['a','t','c','g']

print(mySequenceAsAList[0])
print(mySequenceAsAList[3])
print(mySequenceAsAList[-1])
print(mySequenceAsAList[0:4])
print(mySequenceAsAList[:4])
print(mySequenceAsAList[2:3])
print(mySequenceAsAList[2:4])
print(mySequenceAsAList[2:])
print(mySequenceAsAList[-3:])


myList = ['atcg',['a','t','c','g'],42,True,None]

print('Length of myList is: ',len(myList))
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])
print(myList[1][2])
print(myList[1][1:3])
print()

correctSpelling = 'recognize'

correctSpelling = ['r','e','c','o','g','n','i','z','e']

correctSpelling[7] = 's'
print(correctSpelling)

# The following code doesn't work - strings cannot be edited like this
# Uncomment the [correctSpelling[7] = 's'] line and try to run it to see the error message
correctSpelling = 'recognize'
#correctSpelling[7] = 's'
print(correctSpelling)

correctSpelling = 'recognize'
correctSpelling = correctSpelling.replace('s','z')
print(correctSpelling)


myList = ['apple','banana','pear','llama','orange']
print(myList)
myList.append('peach')
print(myList)
myList.insert(2,'kiwi')
print(myList)
myList.remove('llama')
print(myList)
myList[4] = 'lemon'
print(myList)
print(sorted(myList))


musician = {'name':'Nigel','instrument':'guitar','preferred volume':11,}
print(musician['name'])
print(musician['instrument'])
print(musician['preferred volume'])


gene = {'name':'p53','taxonomy':9606,'metal binding':True,'locations':['cytoplasm','nucleus']}
print(gene['name'])
print(gene['taxonomy'])
print(gene['metal binding'])
print(gene['locations'])
print(gene['locations'][0])
print(gene['locations'][1])


def oligoMolecularWeight(sequence):
    dnaMolecularWeight = {'a':313.2,'c':289.2,'t':304.2,'g':329.2}
    molecularWeight = 0.0
    for base in sequence:
        molecularWeight += dnaMolecularWeight[base]
    return molecularWeight

dnaSequence = 'tagcgctttatcg'
print(oligoMolecularWeight(dnaSequence))


restrictionEnzymes = {}
restrictionEnzymes['bamH1'] = ['ggatcc',0]
restrictionEnzymes['sma1'] = ['cccggg',2]

print(list(restrictionEnzymes.keys()))
print('sma1' in restrictionEnzymes)
print('EcoR1' in restrictionEnzymes)
print(sorted(restrictionEnzymes.keys()))


mySequence = 'gctgtatttcgatcgatttatgct'
print(mySequence.find('ttt'))
print(mySequence.find('ttt',7))
print(mySequence.find('gtgtgt',7))


found = 0
searchFrom = found
while found != -1:
    found = mySequence.find('ttt',searchFrom)
    if found != -1:
        print('Substring found at: ',found)
    searchFrom = found + 1


fruit = ['apple','orange']
print(fruit)
fruit[1] = 'pear'
print(fruit)


fruit = ('apple','orange')
print(fruit)


# The following code doesn't work - tuples are immutable and cannot be edited
# Uncomment the [fruit[1] = 'pear'] line and try to run it to see the error message
#fruit[1] = 'pear'

def restrictionDigest(sequence,enzyme):
    motif = restrictionEnzymes[enzyme][0]
    cutPosition = restrictionEnzymes[enzyme][1]
    fragments = []
    found = 0
    lastCut = found
    searchFrom = lastCut
    while found != -1:
        found = sequence.find(motif,searchFrom)
        if found != -1:
            fragment = sequence[lastCut:found+cutPosition]
            mwt = oligoMolecularWeight(fragment)
            fragments.append((fragment,mwt))
        else:
            fragment = sequence[lastCut:]
            mwt = oligoMolecularWeight(fragment)
            fragments.append((fragment,mwt))
        lastCut = found + cutPosition
        searchFrom = lastCut + 1
    return fragments

digestSequence = 'gcgatgctaggatccgcgatcgcgtacgatcgtacgcggtacggacggatccttctc'
print(restrictionDigest(digestSequence,'bamH1'))
