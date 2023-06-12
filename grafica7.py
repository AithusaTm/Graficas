import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(0,4*np.pi,100)
def f(t):
    return (np.sin(3*tpoints)*(np.cos(2*tpoints)))
plt.plot(tpoints,f(tpoints),'o:c', ms=10)
plt.title('$f(t)=sin(3t)*cos(2t)$\n$g(t)=(1/2)*cos(t))+(5/2)(cos(5t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (0.5*np.cos(tpoints)+(5/2)*np.cos(5*tpoints))
plt.plot(tpoints,y(tpoints),'o:m', ms =10)
plt.legend(['$f(t)$','$g(t)$'])
plt.show()