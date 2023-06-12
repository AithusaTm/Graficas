import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(0,2*np.pi,100)
def f(x):
    return (xpoints*np.exp(-3*xpoints))
plt.plot(xpoints,f(xpoints),'o:c',ms=10)
plt.title('$f(x)=xe^{-3x}$\n$g(x)=1-3xe^{-3x}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(x):
    return (1-(3*xpoints*np.exp(-3*xpoints)))
plt.plot(xpoints,y(xpoints),'o:m', ms=10)
plt.legend(['f(x)','g(x)'])
plt.show()