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
y1 = 5*np.sin(theta)
y2 = 10*np.cos(theta)
plt.plot(180/np.pi*theta, y1, 'r--o', label="sine")
plt.plot(180/np.pi*theta, y2, 'g-*', label="cosine")
plt.legend()
plt.xlabel("Theta")
plt.ylabel("Y")
plt.title("Trigonometric Functions", fontsize=15)
plt.xlim(0, 360)
plt.ylim(-10, 10)
plt.grid()
plt.show()
