import numpy as np
from matplotlib import pyplot as plt

xpoints =  np.linspace(-1, 5, 100)

def f(x):
    return((2*xpoints**2) - (8*xpoints) - 11)
plt.plot(xpoints, f(xpoints), 'o:c', ms = 10)
plt.title("Grafica")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()