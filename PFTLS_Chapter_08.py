#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 8

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


# 1) read in chromosome co-ordinates and name of a FASTQ files
# 2) align the reads in the FASTQ file against the genome generating an aligned BAM file
# 3) extract a subset of reads and save to a new BAM file using pysam
# 4) sort and index the new BAM file

import sys
import os.path
import pysam
import argparse
import subprocess

def sort_and_index(bam_filename):
    prefix, suffix = os.path.splitext(bam_filename)
    
    # generated sorted bam filename
    sorted_bamfilename = prefix + ".sorted.bam"

    # sort output using pysam's output
    print("generate sorted BAM:", sorted_bamfilename)
    pysam.sort("-o", sorted_bamfilename, bam_filename)

    # index output using pysam's index
    print("index BAM:", sorted_bamfilename)
    pysam.index(sorted_bamfilename)

    return sorted_bamfilename

parser = argparse.ArgumentParser(description="""Given an input FASTQ file, align to genome, extract reads for specified region: CHROM:START-END
and write to sorted indexed bam to OUTPUT""")

parser.add_argument('input_fastq', help='input FASTQ file name')
parser.add_argument('-o', '--output', dest="output_final_bam_filename", help='output BAM file name', default="final.bam")
parser.add_argument('-c', '--chrom', help='chromosome name', required=True)
parser.add_argument('-s', '--start', type=int, help='start position on chromosome', required=True)
parser.add_argument('-e', '--end', type=int, help='end position on chromosome', required=True)

# next get and parse args and assign to our local files
args = parser.parse_args()
input_fastq = args.input_fastq
output_final_bam_filename = args.output_final_bam_filename
chrom = args.chrom
start = args.start
end = args.end

# get prefix and extension from FASTQ file
prefix, suffix = os.path.splitext(input_fastq)

output_sam_filename = prefix + '.sam'
output_bam_filename = prefix + '.bam'

# using subprocess need to generate the standard output *first*
with open(output_sam_filename, "w") as output_sam:
    # do the alignment, note that we hardcode the genome we align against to the bacterial genome
    print("generated SAM output from:", input_fastq)
    subprocess.check_call(['bwa', 'mem', 'NC_008253.fna', input_fastq], stdout=output_sam)

# convert back to the binary (compressed) BAM format using samtools
with open(output_bam_filename, "wb") as output_bam:
    subprocess.check_call(['samtools', 'view', '-b', '-S', output_sam_filename], stdout=output_bam)

output_sorted_bamfilename = sort_and_index(output_bam_filename)

# set bamfile status
read_count = 0

print("now extract reads from:", output_sorted_bamfilename)
all_reads = pysam.AlignmentFile(output_sorted_bamfilename, 'rb')

# create final output file
output_final_bam = pysam.AlignmentFile(output_final_bam_filename, 'wb', template=all_reads)

# use pysam to extract the reads from the given co-ordinates
print("extract reads from chromosome:" + chrom + "at coordinates:", start, end)
output_reads= all_reads.fetch(chrom, start, end)

for read in output_reads:
    read_count += 1
    output_final_bam.write(read)
all_reads.close()

print("saving new BAM:", output_final_bam_filename, " with", read_count, "reads aligning in %s:%d-%d" % (chrom, start, end))
output_bam.close()  # finally close the output bam file
sort_and_index(output_final_bam_filename) # sort and index
