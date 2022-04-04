import numpy as np
import scipy as s
import random as r
from scipy.spatial.distance import cityblock
from numpy import linalg as lg
import matplotlib.pyplot as plt



def computeL (U, V):
    L1 = cityblock(U,V)
    L2 = lg.norm(U-V) ** 2
    print("L1 loss = " + str(L1))
    print("L2 loss = " + str(L2))

    return L1,L2
 
# B) C) Generate random vectors U and V with a max of M = 50
M = r.randint(0,50)
u = np.random.randint(r.randint(-100,0), r.randint(0,100), size=(M,1))
v = np.random.randint(r.randint(-100,0), r.randint(0,100), size=(M,1))
x = abs(u - v)

print(x)
L = computeL(u,v)

# A) Generate a random x-axis vector in the range -1,1 with 100 points
x_vals = np.linspace(-1,1, num=100)

# given that the x_vals is the |u-v| vector, find the L1 and L2 and set them to y1 and y2 respectively
y1 = np.sum(x_vals)
y2 = lg.norm(x_vals) ** 2
y_1 = np.full((100,1), y1)
y_2 = np.full((100,1), y2)
print(x_vals)
plt.plot(x_vals, y_1, 'bo', x_vals, y_2, 'go')
plt.show()


#print(u)
#print(v)
#print(x)