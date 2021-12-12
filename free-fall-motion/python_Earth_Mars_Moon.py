import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# time array
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0, t_end+dt, dt)

# gravitational accelerations
g_Earth = -9.8  # [m/s^2]
g_Mars = -3.7  # [m/s^2]
g_Moon = -1.6  # [m/s^2]

# position y arrays
n = 2
y_i = 100  # [m]
y_Earth = y_i+0.5*g_Earth*t**n
y_Mars = y_i+0.5*g_Mars*t**n
y_Moon = y_i+0.5*g_Moon*t**n
# np.set_printoptions(suppress=True)

# velocity y arrays
y_Earth_velocity = n*0.5*g_Earth*t**(n-1)
y_Mars_velocity = n*0.5*g_Mars*t**(n-1)
y_Moon_velocity = n*0.5*g_Moon*t**(n-1)

# acceleration y arrays
y_Earth_acceleration = (n-1)*g_Earth*t**(n-2)
y_Mars_acceleration = (n-1)*g_Mars*t**(n-2)
y_Moon_acceleration = (n-1)*g_Moon*t**(n-2)

# Create circles


def create_circle(r):
    degrees = np.arange(0, 361, 1)
    radians = degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y


radius_Earth = 5  # [meters]
radius_Mars = 10  # [meters]
radius_Moon = 20  # [meters]
sphere_x_Earth, sphere_y_Earth = create_circle(radius_Earth)
sphere_x_Mars, sphere_y_Mars = create_circle(radius_Mars)
sphere_x_Moon, sphere_y_Moon = create_circle(radius_Moon)

# np.set_printoptions(suppress=True)
# print(sphere_x_Earth)
# print(sphere_y_Earth)
# exit()

############################## ANIMATION ##################################
frame_amount = len(t)
width_ratio = 1.2
y_f = -10  # [m]
dy = 10  # [m]


def update_plot(num):
    if y_Earth[num] >= radius_Earth:
        spehere_Earth.set_data(sphere_x_Earth, sphere_y_Earth+y_Earth[num])
        alt_E.set_data(t[0:num], y_Earth[0:num])
        vel_E.set_data(t[0:num], y_Earth_velocity[0:num])
        acc_E.set_data(t[0:num], y_Earth_acceleration[0:num])

    if y_Mars[num] >= radius_Mars:
        spehere_Mars.set_data(sphere_x_Mars, sphere_y_Mars+y_Mars[num])
        alt_Ma.set_data(t[0:num], y_Mars[0:num])
        vel_Ma.set_data(t[0:num], y_Mars_velocity[0:num])
        acc_Ma.set_data(t[0:num], y_Mars_acceleration[0:num])

    if y_Moon[num] >= radius_Moon:
        spehere_Moon.set_data(sphere_x_Moon, sphere_y_Moon+y_Moon[num])
        alt_Mo.set_data(t[0:num], y_Moon[0:num])
        vel_Mo.set_data(t[0:num], y_Moon_velocity[0:num])
        acc_Mo.set_data(t[0:num], y_Moon_acceleration[0:num])

    return spehere_Earth, spehere_Mars, spehere_Moon, alt_E, alt_Ma, alt_Mo,\
        vel_E, vel_Ma, vel_Mo, acc_E, acc_Ma, acc_Mo


# Figure properties
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 4)

# Create object for Earth
ax0 = fig.add_subplot(gs[:, 0], facecolor=(0.9, 0.9, 0.9))
spehere_Earth, = ax0.plot([], [], 'k', linewidth=3)
land_Earth = ax0.plot(
    [-radius_Earth*width_ratio, radius_Earth*width_ratio], [-5, -5], linewidth=38)
plt.xlim(-radius_Earth*width_ratio, radius_Earth*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius_Earth, radius_Earth+1, radius_Earth))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude [m]')
plt.title('Earth')
copyright = ax0.text(-radius_Earth*width_ratio, (y_i+10)
                     * 3.2/3, '© Nhat Vu', size=12)


# Create object for Mars
ax1 = fig.add_subplot(gs[:, 1], facecolor=(0.9, 0.9, 0.9))
spehere_Mars, = ax1.plot([], [], 'k', linewidth=3)
land_Mars = ax1.plot([-radius_Mars*width_ratio, radius_Mars *
                     width_ratio], [-5, -5], 'orangered', linewidth=38)
plt.xlim(-radius_Mars*width_ratio, radius_Mars*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius_Mars, radius_Mars+1, radius_Mars))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.title('Mars')


# Create object for Moon
ax2 = fig.add_subplot(gs[:, 2], facecolor=(0.9, 0.9, 0.9))
spehere_Moon, = ax2.plot([], [], 'k', linewidth=3)
land_Moon = ax2.plot([-radius_Moon*width_ratio, radius_Moon *
                     width_ratio], [-5, -5], 'gray', linewidth=38)
plt.xlim(-radius_Moon*width_ratio, radius_Moon*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius_Moon, radius_Moon+1, radius_Moon))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.title('Moon')


# Create position function
ax3 = fig.add_subplot(gs[0, 3], facecolor=(0.9, 0.9, 0.9))
alt_E, = ax3.plot([], [], '', linewidth=3, label='Alt_Earth = ' +
                  str(y_i)+' + ('+str(round(g_Earth/2, 1))+')t^'+str(n)+' [m]')
alt_Ma, = ax3.plot([], [], 'orangered', linewidth=3, label='Alt_Mars = ' +
                   str(y_i)+' + ('+str(round(g_Mars/2, 1))+')t^'+str(n)+' [m]')
alt_Mo, = ax3.plot([], [], 'gray', linewidth=3, label='Alt_Moon = ' +
                   str(y_i)+' + ('+str(round(g_Moon/2, 1))+')t^'+str(n)+' [m]')
plt.xlim(0, t_end)
plt.ylim(0, y_i)
plt.legend(loc=(0.6, 0.7), fontsize='x-small')

# Create velocity function
ax4 = fig.add_subplot(gs[1, 3], facecolor=(0.9, 0.9, 0.9))
vel_E, = ax4.plot([], [], '', linewidth=3,
                  label='Vel_Earth = '+str(g_Earth)+'t [m/s]')
vel_Ma, = ax4.plot([], [], 'orangered', linewidth=3,
                   label='Vel_Mars = '+str(g_Mars)+'t [m/s]')
vel_Mo, = ax4.plot([], [], 'gray', linewidth=3,
                   label='Vel_Moon = '+str(g_Moon)+'t [m/s]')
plt.xlim(0, t_end)
plt.ylim(y_Earth_velocity[-1], 0)
plt.legend(loc='lower left', fontsize='x-small')

# Create acceleration function
ax5 = fig.add_subplot(gs[2, 3], facecolor=(0.9, 0.9, 0.9))
acc_E, = ax5.plot([], [], '', linewidth=3,
                  label='Acc_Earth = '+str(g_Earth)+' [(m/s)/s ≡ m/s^2]')
acc_Ma, = ax5.plot([], [], 'orangered', linewidth=3,
                   label='Acc_Mars = '+str(g_Mars)+' [(m/s)/s ≡ m/s^2]')
acc_Mo, = ax5.plot([], [], 'gray', linewidth=3,
                   label='Acc_Moon = '+str(g_Moon)+' [(m/s)/s ≡ m/s^2]')
plt.xlim(0, t_end)
plt.ylim(g_Earth-1, 0)
plt.legend(loc=(0.02, 0.25), fontsize='x-small')


plane_ani = animation.FuncAnimation(fig, update_plot,
                                    frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()


#############################
