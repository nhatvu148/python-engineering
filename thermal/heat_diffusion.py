import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

L = 5  		# lenght of the rod
nx = 150  	# number of points on the length
T = 10  	# total time of the simulation
nt = 200 	# number of time steps

x = np.linspace(0, L, nx)

k = 0.2		# heat constant
h = L / (nx - 1)

dudt = []


def diff_fun(u, t):

    dudt = np.ones(x.shape)

    dudt[0] = 0
    dudt[-1] = 0

    for i in range(1, nx-1):
        dudt[i] = k * (u[i + 1] - 2*u[i] + u[i - 1]) / h**2

    return dudt


t_max = 150

in_temp = t_max*np.ones(x.shape)*np.sin(np.pi*x/L)

tspan = np.linspace(0.0, T, nt)
sol = odeint(diff_fun, in_temp, tspan)

for i in range(len(tspan)):

    plt.clf()
    plt.plot(x, sol[0], color='black', label='Initial Temperature profile')
    plt.plot(x, sol[i], color='salmon', label='Current Temperature profile')
    heading = 'Time $t$ = ' + \
        str(tspan[i])+' s, $T_{max}$ = '+str(np.amax(sol[i]))+' $^o C$'
    plt.suptitle(heading)
    plt.title('Heat Diffusion in Rod - 1D')
    plt.xlim(0, L)
    plt.ylim(0, t_max+20)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('T(X)')
    #plt.title('t = {0}'.format(tspan[i]))
    plt.legend()
    plt.pause(0.01)
