# -*- coding: utf-8 -*-
"""
Created on Sun May 01 21:59:13 2016

@author: Yuqi Wang   2013301020086
"""
import math as math
import pylab as pl

q = 0.5
omega = 2. / 3. + 0.001
F = 1.2
end_t = 10000.
T = 2 * math.pi / omega
num = int(T / (0.01 * math.pi))

class state:
    def __init__(self, _theta, _w, _t):
        self.theta = _theta
        self.w = _w
        self.t = _t
        
class pendulum:
    def __init__(self, _state = state(0, 0, 0), _dt = 0.01 * math.pi):
        self.states = []
        self.states.append(_state)
        self.dt = _dt
    def a(self, current_state):
        a = - math.sin(current_state.theta) - q * current_state.w + F * math.sin(omega * current_state.t)
        return a
    def next_state(self, current_state):
        next_w = current_state.w + self.a(current_state) * self.dt
        temp = current_state.theta + next_w * self.dt
        next_theta = self.correct(temp)
        return state(next_theta, next_w, current_state.t + self.dt)
    def correct(self, temp):
        if temp > math.pi:
            temp = temp - 2 * math.pi
        elif temp < - math.pi:
            temp = temp + 2 * math.pi
        return temp
    def run(self):
        for i in range(int(end_t / self.dt)):
            self.states.append(self.next_state(self.states[-1]))
    def draw(self):
        counter = 0
        all_theta = []
        all_w = []
        all_t = []
        attract_theta = []
        attract_w = []
        attract_t = []
        for s in self.states:
            all_theta.append(s.theta)
            all_w.append(s.w)
            all_t.append(s.t)
            if counter%num == 0:
                attract_theta.append(s.theta)
                attract_w.append(s.w)
                attract_t.append(s.t)
            counter = counter + 1
        pl.figure(figsize=(30,18),dpi=96)
        #pl.plot(all_theta,all_w,linestyle='-',linewidth=1.0,color='b',label='F=1.2')
        #pl.plot(all_t,all_theta,linestyle='-',linewidth=1.0,color='r',label='alpha=3')
        pl.xlabel('$\Theta$')
        pl.ylabel('$\omega$')
        pl.title('attraction')
        pl.scatter(attract_theta, attract_w, label = '$\Omega=2/3+0.001$'+'\n'+'$F_D=1.2$')
        pl.legend(loc='upper right', fontsize= 16)

x = pendulum(state(0.2, 0., 0.))
x.run()
x.draw()
pl.show()
        
