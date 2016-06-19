from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
data = open("wavefunction.txt", "r")
x = []
y = []
psi = []
i = 0
for row in data:
    values = row.split()
    for j in range(len(values)):
        temp = float(values[j])
        psi.append(temp)
        y.append(j)
        x.append(i)
    i += 1

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, psi, c = 'r', marker = '.')
plt.show()
