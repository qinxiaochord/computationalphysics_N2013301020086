import math
import pylab as plb

g = 9.8
a = 6.5 * 10**(-3)
alpha = 2.5
T = 300
B2m = 4 * 10**(-5)

def caculate_free(dt):
    x_free = [0]
    y_free = [0]
    t = [0]
    vx_free = [initSpeed * math.cos(theta), initSpeed * math.sin(theta)]
    vy_free = [initSpeed * math.cos(theta), initSpeed * math.sin(theta)]
    i = 1    
    while True:
        x = x_free[-1]
        y = y_free[-1]
        vx = vx_free[-1]
        vy = vy_free[-1]
        x_free.append(x + vx * dt)
        y_free.append(y + vy * dt)
        vx_free.append(vx)
        vy_free.append(vy - g * dt)
        t.append(i * dt)
        if y_free[-1] < 0 and vy_free[-1] < 0:
            break
    l_free = len(x_free)
    return x_free, y_free, vx_free, vy_free, l_free

def caculate_drag(dt):
    x_drag = [0]
    y_drag = [0]
    t = [0]
    vx_drag = [initSpeed * math.cos(theta), initSpeed * math.sin(theta)]
    vy_drag = [initSpeed * math.cos(theta), initSpeed * math.sin(theta)]
    i = 1    
    while True:
        x = x_drag[-1]
        y = y_drag[-1]
        vx = vx_drag[-1]
        vy = vy_drag[-1]
        v = math.sqrt(vx**2 + vy**2)
        x_drag.append(x + vx * dt)
        y_drag.append(y + vy * dt)
        vx_drag.append(vx - B2m * vx * v * (1 - a * y / T)**alpha * dt)
        vy_drag.append(vy - g * dt - B2m * vy * v * (1 - a * y / T)**alpha * dt)
        t.append(i * dt)        
        if y_drag[-1] < 0 and vy_drag[-1] < 0:
            break
    l_drag = len(x_drag)
    return x_drag, y_drag, vx_drag, vy_drag, l_drag

angle = float(raw_input('please input the firing angle : '))
initSpeed = float(raw_input('please input the firing speed : '))
dt = float(raw_input('please input the time interval : '))
theta = angle * 2 * math.pi / 360
x_free, y_free, vx_free, vy_free, l_free = caculate_free(dt)
x_drag, y_drag, vx_drag, vy_drag, l_drag = caculate_drag(dt)



print 'Now print the data without drag : '
for i in range(l_free):
    print x_free[i], y_free[i], vx_free[i], vy_free[i]

print 'Now print the data with drag : '
for i in range(l_drag):
    print x_drag[i], y_drag[i], vx_drag[i], vy_drag[i]


plb.figure(figsize=(10,6),dpi=144)
plb.plot(x_free,y_free,linestyle='-',linewidth=1.0,color='b',label='without drag')
plb.plot(x_drag,y_drag,linestyle='--',linewidth=1.0,color='r',label='with drag')
plb.title('y vs x')
plb.xlabel=('x axis')
plb.ylabel=('y axis')
plb.legend(loc='upper right',fontsize=14)
plb.show()
