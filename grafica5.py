import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(0,4*np.pi,200)
def r(x):
    return (np.cos(2*xpoints)+np.sin(3*xpoints))
plt.plot(xpoints,r(xpoints),'o:b', ms = 2)
plt.title('$s(x)=cos2x+sin2x$\n$v(x)=-2sin2x+3cos3x$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def s(x):
    return (-2*np.sin(2*xpoints)+3*np.cos(3*xpoints))
plt.plot(xpoints,s(xpoints),'o:r', ms = 2)
plt.legend(['$s(x)$','$v(x)$'])
plt.show()
