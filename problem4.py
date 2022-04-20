import numpy as np
import scipy as s
import random as r
from scipy.spatial.distance import cityblock
from numpy import linalg as lg
import matplotlib.pyplot as plt

v1 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))
v2 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))
<<<<<<< HEAD:A5/problem4.py
v3 = np.random.randint(r.randint(-10,0), r.randint(0,10), size=(3,1))
 
=======

numer = v1.T @ v2
denom = lg.norm(v2)
proj = (numer/denom)*v2

print("U = ")
>>>>>>> cf95d12ae915d8ca705e8d4df8c378f40f125f65:problem4.py
print(v1)
print("V = ")
print(v2)
print("proj =")
print(proj)

ax = plt.figure().add_subplot(projection='3d')


origin = np.array([[0, 0, 0], [0, 0, 0], [0,0,0]])

<<<<<<< HEAD:A5/problem4.py
ax.quiver(*origin, v1, v2, v3, normalize=True)
=======
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.quiver(*origin, v1, v2, proj, normalize=True)
>>>>>>> cf95d12ae915d8ca705e8d4df8c378f40f125f65:problem4.py

plt.show()