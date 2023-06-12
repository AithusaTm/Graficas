import numpy as np
from matplotlib import pyplot as plt
import math

tpoints = np.linspace(0,2*np.pi,100)
def h(t):
    return (np.sin(3*t))
plt.plot(tpoints,h(tpoints),'o:c', ms=10)
plt.title('$x=sin(3t)$\n$y=sin(4t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def j(t):
    return (np.sin(4*t))
plt.plot(tpoints,j(tpoints),'o:m', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.show()