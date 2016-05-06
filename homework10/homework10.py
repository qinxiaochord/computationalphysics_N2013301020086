'''
Created on May 4th, by 2013301020086  Yuqi Wang.
'''

import pylab as pl

end_t = 50
sigma = 10
b = 8. / 3.
error = 0.0001 
r = 22

class state:
    def __init__(self, _x, _y, _z, _v_x, _v_y, _v_z, _t):
        self.x = _x
        self.y = _y
        self.z = _z
        self.v_x = _v_x
        self.v_y = _v_y
        self.v_z = _v_z
        self.t = _t

class fluid:
    def __init__(self, _state = state(0, 0, 0, 0, 0, 0, 0), _dt = 0.0001):
        self.states = []
        self.states.append(_state)
        self.dt = _dt
    def next_state(self, current_state):
        next_v_x = sigma * (current_state.y - current_state.x)
        next_v_y = -current_state.x * current_state.z + r * current_state.x - current_state.y
        next_v_z = current_state.x * current_state.y - b * current_state.z
        next_x = current_state.x + next_v_x * self.dt
        next_y = current_state.y + next_v_y * self.dt
        next_z = current_state.z + next_v_z * self.dt
        return state(next_x, next_y, next_z, next_v_x, next_v_y, next_v_z, current_state.t + self.dt)
    def run(self):
        for i in range(int(end_t / self.dt)):
            self.states.append(self.next_state(self.states[-1]))
    def show(self):
        all_x = []
        all_y = []
        all_z = []
        all_v_x = []
        all_v_y = []
        all_v_z = []
        all_t = []
        attractorx_y = []
        attractorx_z = []
        attractory_x = []
        attractory_z = []
        for i in range(len(self.states)):
            all_x.append(self.states[i].x)
            all_y.append(self.states[i].y)
            all_z.append(self.states[i].z)
            all_v_x.append(self.states[i].v_x)
            all_v_y.append(self.states[i].v_y)
            all_v_z.append(self.states[i].v_z)
            all_t.append(self.states[i].t)
            if self.states[i].x * self.states[i - 1].x < 0:
                r = self.states[i].x / (self.states[i - 1].x - self.states[i].x)
                attractorx_y.append(self.states[i - 1].y * (1 - r) + self.states[i].y * r)
                attractorx_z.append(self.states[i - 1].z * (1 - r) + self.states[i].z * r)
            if self.states[i].y * self.states[i - 1].y < 0:
                r = abs(self.states[i].y / self.states[i - 1].y)
                attractory_x.append((self.states[i - 1].x * r + self.states[i].x) / (1 + r))
                attractory_z.append((self.states[i - 1].z * r + self.states[i].z) / (1 + r))
        pl.figure(figsize=(30,18), dpi = 96)
        self.plot_x_z(all_x, all_z)
        #self.plot_t_z(all_t, all_z)
        #self.attractor_y_z(attractorx_y, attractorx_z)
        #self.attractor_x_z(attractory_x, attractory_z)
        pl.legend(loc = 'upper right', fontsize = 16)
        pl.show()
    def plot_x_z(self, x, z):
        pl.plot(x, z, color = 'b', label = 'r=22')
        pl.xlabel('x')
        pl.ylabel('z')
        pl.title('phase space plot : z versus x')
    def plot_t_z(self, t, z):
        pl.plot(t, z, color = 'b', label = 'r=163.8')
        pl.xlabel('t')
        pl.ylabel('z')
        pl.title('Lorenz model z versus time')
    def attractor_y_z(self, y, z):
        pl.plot(y, z, color = 'b', label = 'r=25')
        pl.xlabel('y')
        pl.ylabel('z')
        pl.title('phase space plot : z versus y when x=0')
    def attractor_x_z(self, x, z):
        pl.plot(x, z, color = 'b', label = 'r=25')
        pl.xlabel('x')
        pl.ylabel('z')
        pl.title('phase space plot : z versus x when y=0')
a = fluid(state(1, 0, 0, 0, 0, 0, 0))
a.run()
a.show()
    
