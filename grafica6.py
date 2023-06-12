import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(0,2,200)
def f(x):
    return (xpoints*np.exp(-3*xpoints))
plt.plot(xpoints,f(xpoints),'o:c',ms=10)
plt.title('$f(x)= xe^{-3x}$\n$g(x)=e^{-3x}(1-3x)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(x):
    return np.exp(-3*xpoints)*(1-3*xpoints)
plt.plot(xpoints,y(xpoints),'o:m', ms=10)
plt.legend(['f(x)','g(x)'])
plt.show()
