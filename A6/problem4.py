import numpy as np
import scipy as s
import random as r
from scipy.spatial.distance import cityblock
from numpy import linalg as lg
import matplotlib.pyplot as plt


filename = "dataset1.txt"

A = np.loadtxt(filename)


print(A)