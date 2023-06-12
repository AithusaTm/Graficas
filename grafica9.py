import numpy as np
from matplotlib import pyplot as plt
import math

xpoints = np.linspace(0,2*np.pi,100)
def f(x):
    return (np.power(np.cos(xpoints),3))
plt.plot(xpoints,f(xpoints),'o:c', ms=10)
plt.title('$x=cos^{3}(t)$\n$y=sin^{3}(t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def t(x):
    return (np.sin(xpoints)**3)
plt.plot(xpoints,t(xpoints),'o:m', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.show()
