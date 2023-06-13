import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1,1,0.1)
y = np.arange(-1,1,0.1)
x, y = np.meshgrid(x,y)
z = np.cos (np.abs(x) + np.abs(y)) * (np.abs(x) + np.abs(y))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, color='#ab9dc4', linewidth=1)
ax.set_title('Grafica superficies 6: $z=cos(|x| + |y|)*(|x| + |y|)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()