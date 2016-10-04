#!/usr/bin/env python

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 16

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

import turtle
import sys

# Lindenmayer's original L-system for modelling the growth of algae.
# rules : (A -> AB), (B -> A)

def algae_growth(number, output="A", show=False):
    for i in range(number):
        new_output = ""
        for letter in output:
            if letter == "A":        # rule #1
                new_output += "AB"
            elif letter == "B":      # rule #2
                new_output += "A"
        output = new_output
        if show: print "n =", i+1, output, "[", len(output), "]"
    return output

def plant_growth(number, output="X", show=False):

    for i in range(number):
        new_output = ""
        for letter in output:
            # rule #1
            if letter == "X":
                new_output += "F-[[X]+X]+F[+FX]-X"
            elif letter == "F":
                new_output += "FF"
            else:
                new_output += letter
        output = new_output
        if show: print "n =", i+1, output, "[", len(output), "]"
    return output

def draw_plant(actions):

    stk = []
    for action in actions:
        if action=='X':        # do nothing
            pass
        elif action== 'F':     # go forward
            turtle.forward(2)
        elif action=='+':      # rotate right by 25 degrees
            turtle.right(25)
        elif action=='-':      # rotate left by 25 degrees
            turtle.left(25)
        elif action=='[':
            # save the position and heading by "pushing" down on to the stack
            pos = turtle.position()
            head = turtle.heading()
            stk.append((pos, head))
        elif action==']':
            # restore position and heading: by "popping" off the first item from stack
            pos, head = stk.pop()
            turtle.penup()
            turtle.setposition(pos)
            turtle.setheading(head)
            turtle.pendown()
        else:
            raise ValueError("don't recognize action", action)
        
    turtle.update()

print "n = 0", "A", "[ 1 ]"
algae=algae_growth(6, output="A", show=True)

print "n = 0", "X", "[ 1 ]"
plant=plant_growth(6, output="X", show=False)

# get initial position
x = 0
y = -turtle.window_height() / 2

turtle.hideturtle()
turtle.left(90)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
draw_plant(plant)

ts = turtle.getscreen().getcanvas()
ts.postscript(file = "fern.eps")
