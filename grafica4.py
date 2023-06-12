import numpy as np
from matplotlib import pyplot as plt

tpoints =  np.linspace(0, 24, 100)

def h(t):
    return(np.sin(2*tpoints)*np.exp(-0.1*tpoints))
plt.plot(tpoints, h(tpoints), 'o:c')
plt.title('Grafica')
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()