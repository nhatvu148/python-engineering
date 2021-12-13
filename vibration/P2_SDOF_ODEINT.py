# # Single DOF Problem - Scipy ODEINT

# In[20]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def SDOF(state, t):
    M = 500  # Mass
    K = 100  # stiffness
    C = 100  # damping

    F0 = 100
    w = 30

    x, xd = state

    xdd = F0*np.sin(w*t)/M - (C/M)*xd - (K/M)*x

    return [xd, xdd]


initial_cond = [1, 1]
ti = 0
tf = 60
time_step = 0.01

time = np.arange(ti, tf, time_step)

state1 = odeint(SDOF, initial_cond, time)
disp = state1[:, 0]
vel = state1[:, 1]

plt.figure(figsize=(10, 7.5))
plt.subplot(211)
plt.plot(time, disp)
plt.tight_layout(pad=3)

plt.subplot(212)
plt.plot(time, vel)

plt.show()
