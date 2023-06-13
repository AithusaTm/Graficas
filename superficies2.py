import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-2,2,0.2)
y = np.arange(-2,2,0.2)
x, y = np.meshgrid(x,y)
z = x * np.exp ( - x**2 - y**2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(x,y,z,color='m',rstride=1, cstride=1, linewidth=2)
ax.set_title('Grafica superficies 2: $xe^{-x^2-y^2}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()