import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


d = np.zeros((3,3,3))
d[0,:,:] = 1
a = np.rot90(d ,axes=(-1, 0))
b = np.rot90(d ,axes=(-1, 0))
c = np.rot90(d ,axes=(0, 1))
e = np.rot90(d ,axes=(0, -1)) # es igual a la transpuesta rotada
f = d.T
d.nonzero()
a.nonzero()
b.nonzero()
c.nonzero()
e.nonzero()
f.nonzero()
#z,x,y = d.nonzero()
z1,x1,y1 = d.nonzero()
z2,x2,y2 = a.nonzero()
z3,x3,y3 = b.nonzero()
z4,x4,y4 = c.nonzero()
z5,x5,y5 = e.nonzero()
z6,x6,y6 = f.nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.scatter(x1, y1, z1, zdir='z', c= 'blue')
ax.scatter(x2, y2, z2, zdir='z', c= 'red')
#ax.scatter(x3, y3, z3, zdir='z', c= 'green')
#ax.scatter(x4, y4, z4, zdir='z', c= 'black')
#ax.scatter(x5, y5, z5, zdir='z', c= 'orange')
#ax.scatter(x6, y6, z6, zdir='z', c= 'red')
plt.show()
ax.set_xlabel("")
