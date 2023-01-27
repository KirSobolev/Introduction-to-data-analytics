import numpy as np

def read_matrix(file='matrix.txt'):
    data = np.loadtxt(file)
    print(data)
