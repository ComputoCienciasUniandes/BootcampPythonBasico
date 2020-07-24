import numpy as np
import matplotlib.pyplot as plt


def plot_circulo(centro_x, centro_y):
    theta = np.linspace(0.0, 2.0*np.pi, 1000)
    x = centro_x + np.cos(theta)
    y = centro_y + np.sin(theta)
    plt.plot(x, y, color='black')

plt.figure()

# circulo del centro
plot_circulo(0.0, 0.0)

delta_theta = np.pi/3.0
for i in range(6):
    # primera nivel
    theta = np.pi/6.0 + (delta_theta*i)
    r = 1.0
    B = [r*np.cos(theta), r*np.sin(theta)]
    plot_circulo(B[0], B[1])

    # segunda nivel 
    theta = (delta_theta*i)
    r = 2.0*np.cos(np.pi/6.0)
    B = [r*np.cos(theta),r*np.sin(theta)]
    plot_circulo(B[0], B[1])

    # tercera tercer nivel
    theta = np.pi/6.0 + (delta_theta*i)
    r = 2.0
    B = [r*np.cos(theta),r*np.sin(theta)]
    plot_circulo(B[0], B[1])


plt.axis('equal')
plt.savefig("flor_de_la_vida.png")
