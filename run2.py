import matplotlib.pyplot as plt
import numpy as np

# theta from 0 to 360 degrees
theta = np.linspace(0, 2*np.pi, 30)
y1 = 5*np.sin(theta)
y2 = 10*np.cos(theta)

plt.subplot(2, 1, 1)
plt.plot(180/np.pi*theta, y1, 'r--o')
plt.xlabel("Theta")
plt.title("Sine Function", fontsize=15)
plt.xlim(0, 360)
plt.ylabel("Sine")
plt.ylim(-10, 10)
plt.grid()

plt.tight_layout(pad=3.0)

plt.subplot(2, 1, 2)
plt.plot(180/np.pi*theta, y2, 'g-*')
plt.xlabel("Theta")
plt.ylabel("Cosine")
plt.title("Cosine Function", fontsize=15)
plt.xlim(0, 360)
plt.ylim(-10, 10)
plt.grid()
plt.show()
