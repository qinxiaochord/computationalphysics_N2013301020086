# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:49:24 2016

@author: 2013301020086    Yuqi Wang
"""

import math as math
from visual import *

m1 = 100
m2 = 100
m3 = 100
end_t = 1000000
dt = 0.1
t = 0

x10 = 0
y10 = 10
x20 = -5 * math.sqrt(3)
y20 = -5
x30 = 5 * math.sqrt(3)
y30 = -5

v = math.sqrt(10 / math.sqrt(3))
vx10 = v
vy10 = 0
vx20 = - v / 2
vy20 = v * math.sqrt(3) / 2
vx30 = vx20
vy30 = - vy20

body1 = sphere(pos = (x10, y10, 0), radius = 2, color = color.yellow)
body2 = sphere(pos = (x20, y20, 0), radius = 2, color = color.white, material = materials.earth)
body3 = sphere(pos = (x30, y30, 0), radius = 2, color = color.orange, material = materials.wood)
body1.velocity = vector(vx10, vy10, 0)
body2.velocity = vector(vx20, vy20, 0)
body3.velocity = vector(vx30, vy30, 0)
body1.trail = curve(color = body1.color)
body2.trail = curve(color = body2.color)
body3.trail = curve(color = body3.color)

while t < end_t:
    rate(100)
    r12 = math.sqrt((body1.pos.x-body2.pos.x) ** 2 + (body1.pos.y-body2.pos.y) ** 2)
    r23 = math.sqrt((body2.pos.x-body3.pos.x) ** 2 + (body2.pos.y-body3.pos.y) ** 2)
    r31 = math.sqrt((body3.pos.x-body1.pos.x) ** 2 + (body3.pos.y-body1.pos.y) ** 2)
    body1.velocity += m2 * (body2.pos - body1.pos) * dt / r12 ** 3 + m3 * (body3.pos - body1.pos) * dt / r31 ** 3
    body2.velocity += m1 * (body1.pos - body2.pos) * dt / r12 ** 3 + m3 * (body3.pos - body2.pos) * dt / r23 ** 3
    body3.velocity += m1 * (body1.pos - body3.pos) * dt / r31 ** 3 + m2 * (body2.pos - body3.pos) * dt / r23 ** 3
    body1.pos += body1.velocity * dt
    body2.pos += body2.velocity * dt
    body3.pos += body3.velocity * dt
    body1.trail.append(pos = body1.pos)
    body2.trail.append(pos = body2.pos)
    body3.trail.append(pos = body3.pos)
    t += dt
