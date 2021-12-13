#  Diesel Cycle Simulator
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt


def volume(d, s, l, r, theta):
    Vs = (pi/4)*d**2*s
    Vc = Vs/(r-1)
    term1 = 1/(r-1)
    term2 = 1 + (2/s) - cos(theta)
    term3 = sqrt((2/s)**2 + (sin(theta))**2)
    V = Vs*(term1 + 0.5*(term2-term3))

    return V


d = 0.1   # bore
s = 0.1   # stroke
l = 0.15  # length of CR
r = 12    # Compression Ratio

p1 = 101.3
t1 = 300
gamma = 1.4
t3 = 2500

Vs = (np.pi/4) * d**2 * s  # swept volume
Vc = Vs/(r-1)
v1 = Vs + Vc
v2 = Vc
v4 = v1
p2 = p1*(r)**gamma   # adiabatic process - p1v1**gamma = p2v2**gamma
t2 = t1 * r**(gamma-1)
p3 = p2

v3 = v2*t3/t2
p4 = p3*(v3/v4)**gamma

theta = 0

while theta < np.pi:
    theta = theta + 0.001
    v_theata = volume(d, s, l, r, theta)
    if(0 < (v_theata-v3) < 0.001):
        break

print(theta*180/pi)

V_comp = volume(d, s, l, r, np.linspace(0, pi, 180))
P_comp = (p1*v1**gamma)/V_comp**gamma

V_exp = volume(d, s, l, r, np.linspace(pi, theta, 180))
P_exp = (p3*v3**gamma)/V_exp**gamma

plt.figure(figsize=(10, 10))
plt.plot(V_comp, P_comp)
plt.plot([v2, v3], [p2, p3])
plt.plot(V_exp, P_exp)
plt.plot([v4, v1], [p4, p1])

plt.title("PV Diagram Diesel Cycle", fontsize=15)
plt.xlabel("Volume", fontsize=15)
plt.ylabel("Pressure", fontsize=15)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.show()
