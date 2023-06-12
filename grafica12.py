import matplotlib.pyplot as plt
import numpy as np
import math

x=np.arange(0,2*np.pi)
r=2-2*np.sin(x)+(np.sin(x))*(np.sqrt(np.absolute(np.cos(x))))/(np.sin(x)+1.4)
y1= r*np.cos(x)
y2= r*np.sin(x)

plt.subplot(3,1,1)
plt.fill_between(x,0,y1)
plt.ylabel('between y1 and 0')
plt.axis('equal')
plt.axis('off')

plt.subplot(3,1,2)
plt.fill_between(x,y1,1,color='c')
plt.ylabel('between y1 and 1')
plt.axis('equal')
plt.axis('off')

plt.subplot(3,1,3)
plt.fill_between(x,y1,y2)
plt.ylabel('between y1 and y2')
plt.xlabel('x')
plt.axis('equal')
plt.axis('off')
plt.show()