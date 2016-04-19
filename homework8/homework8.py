import pylab as plb

def a(x, k, alpha):
    return - k * x ** alpha

def caculate(x0, v0, k, alpha, end_t, dt):
    x = [x0]
    v = [v0]
    t = [0]
    for i in range(int(end_t / dt)):
        v.append(v[-1] + a(x[-1], k, alpha) * dt)
        x.append(x[-1] + v[-1] * dt)
        t.append(t[-1] + dt)
    return x, t
        
def main():
    x0 = 0.
    v0 = 3.
    k = 1
    alpha = 1
    end_t = 20
    dt = 0.1
    x, t = caculate(x0, v0, k, alpha, end_t, dt)
    beta = 3
    y, t = caculate(x0, v0, k, beta, end_t, dt)
    plb.figure(figsize=(10,6),dpi=144)
    plb.plot(t,x,'ob',linestyle='-',linewidth=1.0,color='b',label='alpha=1')
    plb.plot(t,y,'ob',linestyle='-',linewidth=1.0,color='r',label='alpha=3')
    plb.title('plot x vs t')
    plb.xlabel=('t axis')
    plb.ylabel=('x axis')
    plb.legend(loc='upper right',fontsize=14)
    plb.show()

main()    
