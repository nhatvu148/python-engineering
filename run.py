import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("F(x, y)")
# plt.show()

# theta from 0 to 360 degrees
theta = np.linspace(0, 2*np.pi, 30)
y = 5*np.sin(theta)
plt.plot(180/np.pi*theta, y, 'r--*')
plt.xlabel("Theta")
plt.ylabel("Y")
plt.title("Sine Wave", fontsize=15)
plt.xlim(0, 360)
plt.ylim(-5, 5)
plt.show()
