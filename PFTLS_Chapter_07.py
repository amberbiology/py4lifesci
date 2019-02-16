#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 7

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

# A Python class for handling biological sequences
class Sequence:

    def __init__(self,name,sequence):
        self.name = name
        self.sequence = sequence
        self.residues = {}

    def search(self,pattern):
        return self.sequence.find(pattern)

    def molecularWeight(self):
        mwt = 0.0
        for residue in self.sequence:
            mwt += self.residues[residue]
        return mwt

    def validSequence(self):
        for residue in self.sequence:
            if not residue in self.residues:
                return False
        return True


mySequence = Sequence('Some made up sequence','cgtatgcgct')
print(mySequence.name)
print(mySequence.sequence)
print(mySequence.search('gcg'))


class DNASequence(Sequence):

    def __init__(self,name,sequence):
        Sequence.__init__(self,name,sequence)
        self.residues = {'a':313.2,'c':289.2,'t':304.2,'g':329.2}

    def transcribe(self):
        return self.sequence.replace('t','u')

    def transcribeToRNA(self):
        rnaSequence = self.sequence.replace('t','u')
        rnaName = 'Transcribed from ' + self.name
        return RNASequence(rnaName,rnaSequence)


myDNASequence = DNASequence('My first DNA sequence','gctgatatc')
print(myDNASequence.name)
print(myDNASequence.sequence)
print(myDNASequence.search('gat'))
print(myDNASequence.transcribe())

# This code does not work because mySequence has no transcribe method
# Uncomment the following line to see the error message
#print mySequence.transcribe()

rnaToProtein = {'uuu':'F','uuc':'F','uua':'L','uug':'L',
                'ucu':'S','ucc':'S','uca':'S','ucg':'S',
                'uau':'Y','uac':'Y','uaa':'STOP','uag':'STOP',
                'ugu':'C','ugc':'C','uga':'STOP','ugg':'W',
                'cuu':'L','cuc':'L','cua':'L','cug':'L',
                'ccu':'P','ccc':'P','cca':'P','ccg':'P',
                'cau':'H','cac':'H','caa':'Q','cag':'Q',
                'cgu':'R','cgc':'R','cga':'R','cgg':'R',
                'auu':'I','auc':'I','aua':'I','aug':'M',
                'acu':'T','acc':'T','aca':'T','acg':'T',
                'aau':'N','aac':'N','aaa':'K','aag':'K',
                'agu':'S','agc':'S','aga':'R','agg':'R',
                'guu':'V','guc':'V','gua':'V','gug':'V',
                'gcu':'A','gcc':'A','gca':'A','gcg':'A',
                'gau':'D','gac':'D','gaa':'E','gag':'E',
                'ggu':'G','ggc':'G','gga':'G','ggg':'G'}


class RNASequence(Sequence):

    def __init__(self,name,sequence):
        Sequence.__init__(self,name,sequence)

    def translate(self):
        peptide = []
        for n in range(0,len(self.sequence),3):
            codon = self.sequence[n:n+3]
            peptide.append(rnaToProtein[codon])
        peptideSequence = ''.join(peptide)
        return peptideSequence


myRNASequence = RNASequence('My first RNA sequence','gcugauauc')
print(myRNASequence.name)
print(myRNASequence.sequence)
print(myRNASequence.search('gau'))
print(myRNASequence.translate())


class ProteinSequence(Sequence):

    def __init__(self,name,sequence):
        Sequence.__init__(self,name,sequence)


myProteinSequence = ProteinSequence('My first protein sequence','MDVTLFSLQY')
print(myProteinSequence.name)
print(myProteinSequence.sequence)
print(myProteinSequence.search('LFS'))


newRNASequence = myDNASequence.transcribeToRNA()
print(newRNASequence.name)
print(newRNASequence.sequence)


print(myDNASequence.molecularWeight())
print(myDNASequence.validSequence())


class DNANucleotide:

    nucleotides = {'a': 313.2, 'c': 289.2, 't': 304.2, 'g': 329.2}

    def __init__(self,nuc):
        self.name = nuc
        self.weight = DNANucleotide.nucleotides[nuc]


nucleotide = DNANucleotide('g')
print(nucleotide.name, nucleotide.weight)


class NewDNASequence():

    def __init__(self,name,sequence):
        self.name = name
        self.sequence = []
        for s in sequence:
            d = DNANucleotide(s)
            self.sequence.append(d)

    def molecularWeight(self):
        mwt = 0.0
        for s in self.sequence:
            mwt += s.weight
        return mwt

    def __str__(self):
        nucs = []
        for s in self.sequence:
            nucs.append(s.name)
        return ''.join(nucs)


myDNASequence = NewDNASequence('My new DNA sequence','gctgatatc')
print(myDNASequence.sequence[0])
print(myDNASequence.sequence[0].name)
print(myDNASequence.sequence[0].weight)
print(myDNASequence.molecularWeight())
print(myDNASequence)


a = 10
b = 10.0
c = 'DNA'
d = [1,2,3,4,5]
print(a, b, c, d)
