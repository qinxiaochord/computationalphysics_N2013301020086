#This program solves two coupled ordinary differential equitions
#corresponding to the radiative decay problem involving two types of nuclei.

from pylab import *

NA=[]   #list of numbers of A nucleus
NB=[]   #list of numbers of B nucleus
t=[]    #list of time
NA0=float(raw_input('please input the inicial number of A :'))
NB0=float(raw_input('please input the inicial number of B :'))
tauA=float(raw_input('please input the decay time constant of A :'))
tauB=float(raw_input('please input the decay time constant of B :'))
t_end=float(raw_input('please input how long are the nucleus last :'))
dt=float(raw_input('please input the time interval :'))
NA.append(NA0)
NB.append(NB0)
t0=0    #inicialize t0
t.append(t0)
for i in range(int(t_end/dt)):
    NA.append(NA[i]-NA[i]/tauA)
    NB.append(NB[i]+NA[i]/tauA-NB[i]/tauB)
    i=i+1
    t.append(i*dt)
print t
print NA
print NB
plot(t,NA,'ob',linestyle='-',linewidth=1.0,color='b',label='NA')
plot(t,NB,'or',linestyle='--',linewidth=1.0,color='r',label='NB')
title('plot NA & NB vs t')
xlabel=('t axis')
ylabel=('number axis')
legend(loc='upper right')
show()
