import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
import math as math
data = open("potential.txt", "r")
x = []
y = []
v = []
i = 0
for row in data:
    values = row.split()
    for j in range(len(values)):
        temp = float(values[j])
        v.append(temp)
        y.append(j)
        x.append(i)
    i += 1

fig = pl.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x,y,v,c='r', marker='.')
pl.show()
