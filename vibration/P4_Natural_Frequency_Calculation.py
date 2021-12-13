# Natural Frequencies of system

import numpy as np
from scipy import linalg

m1, m2, m3 = (1, 1, 1)
k1, k2, k3 = (1600, 1600, 1600)

M = np.array([[m1, 0, 0],
              [0, m2, 0],
              [0, 0, m3]])

K = np.array([[k1+k2, -k2, 0],
              [-k2, k2+k3, -k3],
              [0, -k3, k3]])

u, v = linalg.eigh(K, M)

nat_freq = np.sqrt(u)

print("First natural frequency :", nat_freq[0])
print("Second natural frequency :", nat_freq[1])
print("Third natural frequency :", nat_freq[2])
