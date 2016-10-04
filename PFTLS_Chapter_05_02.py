#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 5

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

f = open("Sequences.fasta", 'r')
lines = f.readlines()

seq_dict = {}
seq_name = None  # initially we have not found a gene

for line in lines:
    if line[0] == '>':
        # get name of the gene to use in the dictionary
        seq_name = line[1:].strip()
        seq_dict[seq_name] = ''
    else:
        if seq_name:  # we have a sequence!
            # append the sequence to the dictionary
            seq_dict[seq_name] = seq_dict[seq_name] + line.strip()

print seq_dict
f.close()
