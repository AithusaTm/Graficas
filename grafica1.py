import numpy as np
from matplotlib import pyplot as plt

xpoints =  np.linspace(-6, 2, 200)

def f(x):
    return (5 - (4*xpoints) - (xpoints**2))
plt.plot(xpoints, f(xpoints), 'o:c')
plt.title("Grafica")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()