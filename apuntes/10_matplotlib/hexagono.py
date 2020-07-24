import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0.0, 2.0*np.pi, 7)
x = np.cos(theta)
y = np.sin(theta)

plt.figure()
# vertices externos
plt.plot(x, y, color='black')

# radios internos
for i in range(3):
    plt.plot(x[[0+i,3+i]], y[[0+i,3+i]], color='black')

plt.axis('equal')
plt.savefig("hexagono")
