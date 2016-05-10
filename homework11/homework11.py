# -*- coding: utf-8 -*-
"""
Created on Mon May 09 22:25:30 2016

@author: 2013301020086   Yuqi Wang
"""
import math as math
from visual import *

end_t = 10000.
dt = 1.
t = 0.
Msun = 100
Mearth = 100
x20 = 100
vx20 = 0
vy20 = 1.

earth = sphere(pos = (x20, 0, 0), radius = 5, color = color.white, material = materials.earth)
sun = sphere(pos = (0, 0, 0), radius = 10, color = color.yellow, material = materials.emissive)

earth.velocity = vector(vx20, vy20, 0)
sun.velocity = vector(0, 0, 0)

earth.trail = curve(color = earth.color)
sun.trail = curve(color = sun.color)

earth.trail.append(pos = earth.pos)
sun.trail.append(pos = sun.pos)

while t < end_t:
    rate(100)
    r = math.sqrt((earth.pos.x-sun.pos.x) ** 2 + (earth.pos.y-sun.pos.y) ** 2)
    earth.velocity += Msun * (sun.pos - earth.pos) * dt / r ** 3
    sun.velocity += Mearth * (earth.pos - sun.pos) * dt / r ** 3
    earth.pos += earth.velocity * dt
    sun.pos += sun.velocity * dt
    earth.trail.append(pos = earth.pos)
    sun.trail.append(pos = sun.pos)
    t += dt
