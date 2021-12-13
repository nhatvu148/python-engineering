import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)

z = np.sin(x)*np.cos(y)

plt.contourf(x, y, z, cmap=cm.jet)
plt.show()
