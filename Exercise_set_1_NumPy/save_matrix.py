import numpy as np

def save_matrix(file="matrix.txt"):
    matrix = np.zeros(225).reshape(15, 15)
    np.savetxt(file, matrix)