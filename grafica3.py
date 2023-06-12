import numpy as np
from matplotlib import pyplot as plt

tpoints =  np.linspace(-1, 5, 300)

def f(t):
    return(tpoints*np.exp(-2*tpoints))
plt.plot(tpoints, f(tpoints), 'o:k', ms = 10)
plt.title('$t^-2t$')
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()