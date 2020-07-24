import matplotlib.pyplot as plt
import numpy as np

def planck(l, T):
    h = 6.6E-34 # J s
    c = 2.99E8 # m/s
    k = 1.38E-23 # m^2 kg s^-2 K^-1
    x = (2*h*c**2/l**5)/(np.exp(h*c/(l*k*T))-1) # esto esta en SI
    # Tengo que pasar de W a kW y de m^{-1} a nm^{-1}
    factor  = 1E-3*1E-9
    return factor*x 

l = np.linspace(0.1,3, 100) # en micro metros
temps = [5000,4000,3000] # en K

plt.figure()
for T in temps:
    s = planck(l*1E-6, T)
    plt.plot(l, s)

plt.savefig("cuerpo_negro.png")
