#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 12

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

from numpy import arange
import matplotlib.pyplot as plt

# transcription activation function for a single repressor
def single_repressor(TF_concentration_1, K_D1):
    s = 1/(1 + TF_concentration_1/K_D1 )
    return s

# transcription activation function for a dual repressor
# where repressors interact with strength w
def dual_repressor(TF_concentration_1, TF_concentration_2, K_D1, K_D2, w):
    s = 1/(1 + TF_concentration_1/K_D1 + TF_concentration_2/K_D2 + ((TF_concentration_1/K_D1) * (TF_concentration_2/K_D2))* w)
    return s

def draw_points(TF_ratio, repression, color, linestyle="dashed"):
    plt.axhline(repression,
                linestyle=linestyle,
                color=color,
                linewidth=2)
    plt.annotate("%.1g" % repression,
                 xy = (TF_ratio, repression),
                 xytext = (TF_ratio*0.1, repression*0.1), 
                 color=color,
                 arrowprops=dict(facecolor=color, width=2, frac=0.2, shrink=0.05))

fig1 = plt.figure()

# dissociation constants
K_D1 = 7.9E-10
K_D2 = 25 * K_D1

# single repressor
TF_concentration_1  = arange(0.001, 1000, 0.001) * K_D1
plt.loglog(TF_concentration_1 / K_D1,
           single_repressor(TF_concentration_1, K_D1),
           basex=10, color="blue", label="single", linestyle="dotted", linewidth=2)
plt.xlabel("[TF]/$K_D$")
plt.ylabel("gene expression, $s$")
plt.title('Transcriptional repression')
plt.savefig("Figure-12-3.png", dpi=600)

# dual repressor
w = 200
TF_concentration_2  = arange(0.001, 1000, 0.001) * K_D2
plt.loglog(TF_concentration_2 / K_D2,
           dual_repressor(TF_concentration_2, TF_concentration_2, K_D1, K_D2, w),
           basex=10, color="green", label="dual", linestyle="solid")
plt.savefig("Figure-12-6.png", dpi=600)

for TF_ratio in [0.5, 1.0]:
    plt.axvline(x=TF_ratio, linestyle='dashdot', color='pink', linewidth=3)
    TF_value = TF_ratio * K_D1  # convert ratio into TF concentration
    repression = single_repressor(TF_value, K_D1) 
    draw_points(TF_ratio, repression, "blue", linestyle="dotted")
    TF_value = TF_ratio * K_D2  
    repression = dual_repressor(TF_value, TF_value, K_D1, K_D2, w)
    draw_points(TF_ratio, repression, "green", linestyle="solid")

plt.legend(loc='lower left')
plt.savefig("Figure-12-7.png", dpi=600)
plt.show()

