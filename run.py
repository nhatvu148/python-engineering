import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.25)
y = np.arange(-3, 3, 0.25)
x, y = np.meshgrid(x, y)

R = np.sqrt(x**2 + y**2)
z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)

S1 = ax.plot_surface(x, y, z, cmap=cm.jet)
fig.colorbar(S1)
plt.show()
