import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-1,1,0.1)
y = np.arange(-1,1,0.1)
x, y = np.meshgrid(x,y)
z = np.sin(np.abs(x) - np.abs(y))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z,color='#5fa38a')
ax.set_title('Grafica superficies 4: $z=sen(|x| - |y|)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()