import numpy as np
import scipy as s
import random as r
from scipy.spatial.distance import cityblock
from numpy import linalg as lg
import matplotlib.pyplot as plt

v1 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))
v2 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))
v3 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))

print(v1)
print(v2)

ax = plt.figure().add_subplot(projection='3d')


origin = np.array([[0, 0, 0], [0, 0, 0], [0,0,0]])

ax.quiver(*origin, v1, v2, v3, length=10, normalize=True)

plt.show()