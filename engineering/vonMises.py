import numpy as np
import matplotlib.pyplot as plt

syt = 200  # yield strength MPa

s1 = 125
s2 = 200

s_von = np.sqrt(s1**2-(s1*s2)+s2**2)

a = 2**0.5*syt
b = (2/3)**0.5*syt
alpha = np.linspace(0, 2*np.pi, 360)
theta = np.pi/4

# x = a*np.cos(alpha)
# y = a*np.sin(alpha)
x = (a*np.cos(alpha)*np.cos(theta)) - (b*np.sin(alpha)*np.sin(theta))
y = (a*np.cos(alpha)*np.sin(theta)) + (b*np.sin(alpha)*np.cos(theta))

plt.plot([syt, syt], [0, syt], 'r--')
plt.plot([0, syt], [syt, syt], 'r--')
plt.plot([-syt, 0], [-syt, -syt], 'r--')
plt.plot([-syt, -syt], [0, -syt], 'r--')
plt.plot([0, -syt], [syt, 0], 'r--')
plt.plot([syt, 0], [0, -syt], 'r--')

plt.scatter(s_von, s_von, color='g')
plt.plot(x, y)
plt.show()
