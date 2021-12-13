# Frequency Response For SDOF Multiple Plots

import numpy as np
import matplotlib.pyplot as plt
import math

zeta = [0.05, 0.1, 0.2, 0.3]
r = np.linspace(0, 3, 300)
plt.figure(figsize=(10, 7.5))
for z in zeta:
    a = (1-r**2)
    b = (2*z*r)
    f_resp = 1/np.sqrt(a**2+b**2)
    plt.plot(r, f_resp, label=r'$\zeta={}$'.format(z))
    plt.legend(loc='upper right', fontsize=15)

plt.xlim(r[0], r[-1])
plt.ylim(0, 10)
plt.grid(linestyle='--', color='k')
plt.show()
