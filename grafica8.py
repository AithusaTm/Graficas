import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(0,2*np.pi,100)
def h(t):
    return ((1+np.sin(tpoints))*(np.cos(tpoints)))
plt.plot(tpoints,h(tpoints),'o:c', ms=10)
plt.title('$x(t)=$(1+sin(t))*cos(t)\n$y(t)=(1+2sin(t))*(sin(t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def j(t):
    return (1+(2*np.sin(tpoints))*(np.sin(tpoints)))
plt.plot(tpoints,j(tpoints),'o:m', ms =10)
plt.legend(['$h(t)$','$j(t)$'])
plt.show()