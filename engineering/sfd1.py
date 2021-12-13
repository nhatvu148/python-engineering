import numpy as np
import matplotlib.pyplot as plt

l = 10  # length of beam
udl = 500  # N/m

# Reactions
R = udl*l/2
x = np.linspace(0, l, 100)

X = []
SF = []
M = []

for y in x:
    Mx = (R*y) - udl*(y**2/2)
    sf = R - (udl*y)
    X.append(y)
    M.append(Mx)
    SF.append(sf)

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
