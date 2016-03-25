print 'This program solves two coupled linear ordinary differencial equitions.'

import pylab as plb
import math

NA=[]        #establish a list corresponding to NA
NB=[]        #establish a list corresponding to NB
True_NA=[]   #establish a list corresponding to True NA
True_NB=[]   #establish a list corresponding to True NB
t=[]         #establish a list corresponding to t
NA0=float(raw_input('please input the initial NA :'))
NB0=float(raw_input('please input the initial NB :'))
tauA=float(raw_input('please input the time constant of A tauA :'))
tauB=float(raw_input('please input the time constant of B tauB :'))
t_end=float(raw_input('please input the end time :'))
dt=float(raw_input('please input the time interval :'))
NA.append(NA0)
NB.append(NB0)
True_NA.append(NA0)
True_NB.append(NB0)
t.append(0)
alpha = tauB/tauA
C1 = (NA[0]*alpha-NB[0])/(alpha+1)
C2 = (NA[0]+NB[0])/(alpha+1)
for i in range(int(t_end/dt)):
    NA.append(NA[i]+(NB[i]/tauB-NA[i]/tauA)*dt)
    NB.append(NB[i]+(NA[i]/tauA-NB[i]/tauB)*dt)
    True_NA.append(C1*math.exp(-(i+1)*dt*(alpha+1)/tauB)+C2)
    True_NB.append(-C1*math.exp(-(i+1)*dt*(alpha+1)/tauB)+C2*alpha)
    t.append((i+1)*dt)
print t
print NA
print NB
plb.figure(figsize=(10,6),dpi=144)
plb.plot(t,NA,'ob',linestyle='-',linewidth=1.0,color='b',label='NA(numerical)')
plb.plot(t,NB,'or',linestyle='--',linewidth=1.0,color='r',label='NB(numerical)')
plb.plot(t,True_NA,'^k',linestyle='-',label='Nuclei_a(true)'+' '+r'$A\exp(-\kappa*t)+B$')
plb.plot(t,True_NB,'*k',linestyle='--',label='Nuclei_b(true)'+' '+r'$-C\exp(-\kappa*t)+D$')
plb.title('plot NA & NB vs t')
plb.xlabel=('t axis')
plb.ylabel=('number axis')
plb.legend(loc='upper right',fontsize=8)

plb.show()
