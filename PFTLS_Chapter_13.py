#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 13

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

from string import split, strip

# get the TF regulation data from yeastract
def get_tf_yeastract():

    with open("RegulationTwoColumnTable_Documented_2013927.tsv") as file:
        lines = file.readlines()

    # create two data structures:
    # (1) one indexed by TF
    # (2) one indexed by gene

    # create a dictionary indexed by transcription factors (TF)
    # each key is a TF, each value is a *list* of genes it regulates
    alltfs = {}

    # create a dictionary of indexed by genes
    # each key is a gene, each value is a *list* of TFs regulated by that gene
    allgenes = {}

    for line in lines:

        # split line into elements using ';' as separator
        items = split(line,';')

        # lowercase each item, so that minor typographical differences in
        # casing don't confuse
        items = [item.lower() for item in items]

        # first column  = TF  (element 0)
        # second column = gene that TF regulates (element 1)
        tf = strip(items[0])
        gene = strip(items[1])

        # genes keyed by TF
        if alltfs.has_key(tf):
            # TF already added, we just add the gene
            (alltfs[tf]).add(gene)
        else:
            # otherwise, we create an empty set
            alltfs[tf] = set()
            # then add it
            (alltfs[tf]).add(gene)

        # TFs keyed by gene
        if allgenes.has_key(gene):
            # if gene already exists, we just add the TF
            (allgenes[gene]).add(tf)
        else:
            # otherwise create empty set
            allgenes[gene] = set()
            # then add it
            (allgenes[gene]).add(tf)

    print "total TFs:", len(alltfs)
    print "total genes:", len(allgenes)
    
    return alltfs, allgenes

def get_common_genes(alltfs, tf1, tf2):
    return alltfs[tf1] & alltfs[tf2]

def get_all_genes(alltfs, tf1, tf2):
    return alltfs[tf1] | alltfs[tf2]

if __name__ == "__main__":
    
    # get TF regulation data
    alltfs, allgenes = get_tf_yeastract()

    # remember we lowercased the gene names!
    common_genes = get_common_genes(alltfs, 'abf1', 'cyc8')
    print "genes regulated by both abf1 and cyc8", common_genes

    all_genes = get_all_genes(alltfs, 'abf1', 'cyc8')
    print "genes regulated by abf1 or cyc8", all_genes
