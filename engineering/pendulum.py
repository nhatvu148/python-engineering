import matplotlib.pyplot as plt
from numpy import sin, cos, pi, linspace, arange
from scipy.integrate import odeint
import matplotlib.animation as animation


def pend_motion(state, t):
    m = 1
    g = 9.81
    b = 0.1
    L = 1

    theta, vel = state
    acc = -(b/m) * vel-(g/L) * sin(theta)
    return [vel, acc]


L = 5
state0 = [pi/4, 0]
time_step = 0.01
tf = 60
time = arange(0, tf, time_step)

soln = odeint(pend_motion, state0, time)
disp = soln[:, 0]
vel = soln[:, 1]

x_coord = L*sin(disp)
y_coord = -L*cos(disp)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlim(-L, L)
ax.set_ylim(-L-1, 1)
line, = ax.plot([], [], 'o-', lw=3)
time_template = 'time = %.1fs'
time_text = ax.text(2, 0, '')
ax.grid()


def pend_ani(i):
    thisx = [0, x_coord[i]]
    thisy = [0, y_coord[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*time_step))
    return line, time_text


ani = animation.FuncAnimation(
    fig, func=pend_ani, frames=len(soln), interval=5)

plt.show()
