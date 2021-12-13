import numpy as np
import matplotlib.pyplot as plt

w = 50  # udl N/m
L = 10  # Length of beam

a = 3
b = 5
c = L-(a+b)

R1 = (w*b/L)*(c+b/2)
R2 = (w*b/L)*(a+b/2)
l = np.linspace(0, L, 200)

X = []
SF = []
M = []

for x in l:
    if x < a:
        sf = R1
        m = R1*x
    elif a < x < (a+b):
        sf = R1-(w*(x-a))
        m = (R1*x)-(w*(x-a)**2/2)
    elif x > (a+b):
        sf = -R2
        m = R2*(L-x)

    X.append(x)
    SF.append(sf)
    M.append(m)

plt.figure(figsize=(7.5, 5), dpi=100)
plt.subplot(2, 1, 1)
plt.plot(X, SF, 'g')
plt.fill_between(X, SF, color="green", alpha=0.5, hatch="||")
plt.title("Shear Force Diagram")
plt.ylabel("Shear Force")
plt.tight_layout(pad=4.0)

plt.subplot(2, 1, 2)
plt.plot(X, M, 'r')
plt.fill(X, M, color='red', alpha=0.5, hatch="||")
plt.title("Bending Moment Diagram")
plt.xlabel("Length")
plt.ylabel("Bending Moment")
plt.show()
