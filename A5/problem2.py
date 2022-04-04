import numpy as np
import random as r
from numpy import linalg as lg

def cosine(matrix):
    numer = matrix @ matrix.T # get the numberator dot product of u and v
    #print(numer)
    denom = lg.norm(matrix) * lg.norm(matrix.T)
    out = numer/denom
    print(out)
    return out

M = r.randint(1, 10)
N = r.randint(1, 10)
matrix = np.random.randint(r.randint(-1000,0), r.randint(0,1000), size=(M,N))
print("Matrix m =")
print(matrix)
print("\n\nSimilarity matrix =")
similarity = cosine(matrix)
#print(cos)