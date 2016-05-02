import pylab as plb
import math as math
import numpy as np

def a(theta, w, t, g, l, q, F, omega):
    return - g/l * math.sin(theta) - q * w + F * math.sin(omega * t)

def caculate(theta0, w0, end_t, dt, g, l, q, F, omega, error):
    theta = [theta0]
    w = [w0]
    t = [0]
    theta1 = [theta0]
    w1 = [w0]
    t1 = [0]
    for i in range(int(end_t / dt)):
        w.append(w[-1] + a(theta[-1], w[-1], t[-1], g, l, q, F, omega) * dt)
        temp = theta[-1] + w[-1] * dt
        if temp > math.pi:
            temp = temp -2 * math.pi
        elif temp < - math.pi:
            temp = temp + math.pi
        theta.append(temp)
        t.append(t[-1] + dt)
        if math.fabs(int(t[-1] * omega / (2 * math.pi)) - t[-1] * omega / (2 * math.pi)) < error:
            theta1.append(temp)
            w1.append(w[-1])
            t1.append(t[-1])
    return theta, w, t, theta1, w1, t1
        
def main():
    theta0 = 0.2
    w0 = 0.
    g = 9.8
    l = 9.8
    end_t = 1000000
    dt = 0.04
    q = 0.5
    omega = 2. / 3
    F = 1.2
    error = omega * dt / (2 * math.pi)
    theta, w, t, theta1, w1, t1= caculate(theta0, w0, end_t, dt, g, l, q, F, omega, error)
    plb.figure(figsize=(10,6),dpi=32)
    plb.xlim(-math.pi, math.pi)
    #plb.plot(theta,w,linestyle='-',linewidth=1.0,color='b',label='F=1.2')
    #plb.plot(t,theta,linestyle='-',linewidth=1.0,color='r',label='alpha=3')
    plb.scatter(theta1,w1,linestyle='-',linewidth=1.0,color='b')
    plb.title('plot theta vs t')
    plb.xlabel=('t axis')
    plb.ylabel=('theta axis')
    plb.legend(loc='upper right',fontsize=14)
    plb.show()

main()    