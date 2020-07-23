import numpy as np
import matplotlib.pyplot as plt

coordenadas = np.loadtxt("coordenadas.dat", delimiter=",")
nombres = np.loadtxt("nombres.txt", dtype="str")

plt.figure()
n_ciudades = len(nombres)
for i in range(n_ciudades):
    plt.text(coordenadas[i,1], coordenadas[i,0], nombres[i])
    
plt.scatter(coordenadas[:,1], coordenadas[:,0])
plt.plot(coordenadas[:,1], coordenadas[:,0])

plt.xlabel("Longitud [grados]")
plt.ylabel("Latitud [grados]")
plt.axis('equal')
plt.savefig("ciudades.png")