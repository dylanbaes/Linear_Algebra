import numpy as np
import random as r
from numpy import linalg as lg
import matplotlib.pyplot as plt

def cosine(matrix):
    denom = lg.norm(matrix, axis = 0) 
    matrix = matrix/denom
    numer = matrix.T @ matrix # get the numberator dot product of u and v
    print(numer)
    return numer

M = r.randint(1, 10)
N = r.randint(1, 10)
matrix = np.random.randint(r.randint(-1000,0), r.randint(0,1000), size=(M,N))
print("Matrix m =")
print(matrix)
print("\n\nSimilarity matrix =")
similarity = cosine(matrix)
#print(cos)

plt.matshow(similarity)

plt.show()