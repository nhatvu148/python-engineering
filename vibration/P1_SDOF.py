# # Single degree of Freedom system

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
# variable

M = 500  # Mass
K = 100  # stiffness
C = 100  # damping

time_step = 0.1
F0 = 100
w = 30
end_time = 60

time = np.arange(0, end_time, time_step)

x = np.array([[1], [1]])   # initial [vel,disp]

A = np.array([[M, 0],
              [0, 1]])

B = np.array([[C, K],
              [-1, 0]])

F = np.zeros([2, 1])

disp = []
vel = []
T = []

for t in time:
    F[0] = F0*np.sin(w*t)
    X = x + (time_step * inv(A).dot(F - B.dot(x)))
    x = X
    disp.append(X[1])
    vel.append(X[0])
    T.append(t)

plt.figure(figsize=(10, 7.5))

plt.subplot(211)
plt.plot(T, disp, 'r-', label='Displacement')
plt.legend()
plt.xlim(0, end_time)

plt.subplot(212)
plt.plot(T, vel, 'g', label='Velocity')
plt.legend()


plt.xlim(0, end_time)
plt.show()
