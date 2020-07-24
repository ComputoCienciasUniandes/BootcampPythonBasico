import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0.0, 6.0*np.pi, 1000)
r = theta
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x, y, color='black')
plt.axis('equal')
plt.savefig('espiral.png')

