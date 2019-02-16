#!/usr/bin/env python3

__author__ = 'Amber Biology LLC'

# Python For The Life Sciences
# By Alex Lancaster & Gordon Webster
# Chapter 11

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

import math
import matplotlib.pyplot as plt

class Vector3D:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def unitVector(self):
        m = self.magnitude()
        xu = self.x / m
        yu = self.y / m
        zu = self.z / m
        return Vector3D(xu,yu,zu)

    def rotationMatrix(self,degrees):
        radians = math.radians(degrees)
        u = self.unitVector()
        sa = math.sin(radians)
        ca = math.cos(radians)
        a = ca + u.x * u.x * (1 - ca)
        b = u.x * u.y * (1 - ca) - u.z * sa
        c = u.x * u.z * (1 - ca) + u.y * sa
        d = u.y * u.x * (1 - ca) + u.z * sa
        e = ca + u.y * u.y * (1 - ca)
        f = u.y * u.z * (1 - ca) - u.x * sa
        g = u.z * u.x * (1 - ca) - u.y * sa
        h = u.z * u.y * (1 - ca) + u.x * sa
        i = ca + u.z * u.z * (1 - ca)
        return Matrix3D(a,b,c,d,e,f,g,h,i)


class Matrix3D:

    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def transform3DVector(self,vector):
        tx = self.a * vector.x + self.b * vector.y + self.c * vector.z
        ty = self.d * vector.x + self.e * vector.y + self.f * vector.z
        tz = self.g * vector.x + self.h * vector.y + self.i * vector.z
        return Vector3D(tx,ty,tz)


class Atom:

    def __init__(self,name,x,y,z,q):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.q = q

    def distance(self,other):
        xd = self.x - other.x
        yd = self.y - other.y
        zd = self.z - other.z
        return math.sqrt(xd * xd + yd * yd + zd * zd)

    def electrostatic(self,other):
        r = self.distance(other) * 1.0e-10
        q1 = self.q * 1.6e-19
        q2 = other.q * 1.6e-19
        return 0.000239 * (9.0e9 * 6.02e23 * q1 * q2) / (4.0 * r)


# Define some atoms using coordinates from Human Erythropoietin
serCA = Atom('CA',-44.104,2.133,-16.495,0.07)
serCB = Atom('CB',-45.239,1.307,-17.044,0.05)
serOG = Atom('OG',-44.722,0.368,-18.048,-0.66)
argNH1 = Atom('NH1',-45.692,1.823,-20.906,-0.8)


# Calculate and plot serine OG positions as serine OG is rotated about
# the serine CB-OG bond in 30 degree increments. Also calculate serine
# CB-OG distances to check distance invariance during rotation.
posx = []
posy = []
posz = []
dist = []
rotationAxis = Vector3D(serCA.x - serCB.x,serCA.y - serCB.y,serCA.z - serCB.z)
positionOG = Vector3D(serOG.x-serCB.x,serOG.y-serCB.y,serOG.z-serCB.z)
for angle in range(0,360,30):
    rotMat = rotationAxis.rotationMatrix(float(angle))
    xyzOG = rotMat.transform3DVector(positionOG)
    px = xyzOG.x+serCB.x
    py = xyzOG.y+serCB.y
    pz = xyzOG.z+serCB.z
    posx.append(px)
    posy.append(py)
    posz.append(pz)
    dist.append(math.sqrt((px-serCB.x)**2 + (py-serCB.y)**2 + (pz-serCB.z)**2))
for d in dist:
    print("%.5f" % d, end=' ')
print()
plt.scatter(posx, posy, c=posz, s=100)
plt.gray()
plt.show()


# Calculate and plot distances and electrostatic energies between serine OG
# and arginine NH1 as serine OG is rotated about the serine CB-OG bond in
# 10 degree increments
angleData = []
distData = []
eData = []
incRot = 10
for angle in range(0,360,incRot):
    rotMat = rotationAxis.rotationMatrix(float(angle))
    xyzOG = rotMat.transform3DVector(positionOG)
    rotOG = Atom('OG',xyzOG.x+serCB.x,xyzOG.y+serCB.y,xyzOG.z+serCB.z,-0.66)
    dist = rotOG.distance(argNH1)
    elec = rotOG.electrostatic(argNH1)
    angleData.append(angle)
    distData.append(dist)
    eData.append(elec)
    print(angle,dist,elec)
plt.title('Distance/Electrostatic Energy vs. Bond Rotation')
plt.plot(angleData,eData,"red",angleData,distData,'blue')
plt.axis([0,360,0,20])
plt.xlabel('Rotation Angle (Degrees)')
plt.ylabel('Distance (A)                             E (kCal/mol)')
plt.show()


