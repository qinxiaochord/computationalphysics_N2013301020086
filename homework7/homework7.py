import math as math
from visual import *

g = 9.8
S0m = 4.1e-4

def caculate(initSpeed, theta, w, dt):
    x = [0]
    y = [1.5]
    z = [0]
    vx = [initSpeed * math.cos(theta)]
    vy = [initSpeed * math.sin(theta)]
    vz = [0]
    t = [0]
    i = 1
    while True:
        xt = x[-1]
        yt = y[-1]
        zt = z[-1]
        vxt = vx[-1]
        vyt = vy[-1]
        vzt = vz[-1]
        vt = math.sqrt(vxt**2 + vyt**2 + vzt**2)
        B2m = 0.0039 + 0.0058 / (1 + math.exp(vt - 35) / 5)
        x.append(xt + vxt * dt)
        y.append(yt + vyt * dt)
        z.append(zt + vzt * dt)
        vx.append(vxt - B2m * vt * vxt * dt)
        vy.append(vyt - g * dt)
        vz.append(vzt + S0m * vxt * w * dt)
        t.append(i * dt)
        if y[-1] < 0 and vy[-1] < 0:
            break
    l = len(x)
    return x, y, z, vx, vy, vz, l

angle = float(raw_input('please input the angle of emergence : '))
initSpeed = float(raw_input('please input the initial speed : '))
w = float(raw_input('please input the angular velocity : '))
dt = float(raw_input('please input the time interval : '))
theta = angle * 2 * math.pi / 360
x, y, z, vx, vy, vz, l = caculate(initSpeed, theta, w, dt)

for i in range(l):
    print x[i], y[i], z[i], vx[i], vy[i], vz[i]

ball = sphere(radius = 0.037, color = color.cyan)
ground = box(pos = (50, 0, 0), size = (100, 0.5, 100), color = color.green)
ball.trail = curve(color = ball.color)
for i in range(l):
    rate(20)
    ball.pos = vector(x[i], y[i], z[i])
    ball.trail.append(pos = ball.pos)
