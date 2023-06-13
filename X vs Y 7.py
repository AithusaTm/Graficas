import matplotlib.pyplot as plt
import numpy as np

a= np.arange(0,4 * np.pi, 0.04)
r= - 105 + 100 * np.sin(4.5 * a)
v= a - np.cos(10 * a)/10
x= 320 + r * np.cos(v)
y= - 240 - r * np.sin(v)

plt.plot(x,y,c='k')
plt.title('Grafica X vs Y 7')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.axis('off')
plt.show()