import numpy as np
import matplotlib.pyplot as plt

u = 40
g = 9.81

theta1 = 45
theta2 = 60

ux1 = u*np.cos(theta1*np.pi/180)
uy1 = u*np.sin(theta1*np.pi/180)

ux2 = u*np.cos(theta2*np.pi/180)
uy2 = u*np.sin(theta2*np.pi/180)

t_total_1 = 2*uy1/g
t_total_2 = 2*uy2/g
t1 = np.linspace(0, t_total_1, 100)
t2 = np.linspace(0, t_total_2, 100)

x1 = ux1*t1
y1 = (uy1*t1)-(0.5*g*t1**2)
x2 = ux2*t2
y2 = (uy2*t2)-(0.5*g*t2**2)
plt.plot(x1, y1, label="Theta = 45")
plt.plot(x2, y2, label="Theta = 60")
plt.legend()
plt.show()
