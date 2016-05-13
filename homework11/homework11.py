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
m1 = 100.
m2 = 200.
r0 = 100.
x10 = m2 * r0 / (m1 + m2)
x20 = - m1 * r0 / (m1 + m2)
#circle trajectory
#p0 = math.sqrt(m1 * m1 * m2 * m2 / (r0 * (m1 + m2)))
#ellipse trajectory. remark: p0 <= 2 * mu * m1 * m2 / r0, where mu=m1 * m2 / (m1 + m2) is the reduced mass of the system.
p0 = 90.
vy10 = p0 / m1
vy20 = - p0 / m2

body1 = sphere(pos = (x10, 0, 0), radius = 5, color = color.white, material = materials.earth)
body2 = sphere(pos = (x20, 0, 0), radius = 10, color = color.yellow, material = materials.emissive)

body1.velocity = vector(0, vy10, 0)
body2.velocity = vector(0, vy20, 0)

body1.trail = curve(color = body1.color)
body2.trail = curve(color = body2.color)

body1.trail.append(pos = body1.pos)
body2.trail.append(pos = body2.pos)

while t < end_t:
    rate(100)
    r = math.sqrt((body1.pos.x-body2.pos.x) ** 2 + (body1.pos.y-body2.pos.y) ** 2)
    body1.velocity += m2 * (body2.pos - body1.pos) * dt / r ** 3
    body2.velocity += m1 * (body1.pos - body2.pos) * dt / r ** 3
    body1.pos += body1.velocity * dt
    body2.pos += body2.velocity * dt
    body1.trail.append(pos = body1.pos)
    body2.trail.append(pos = body2.pos)
    t += dt
