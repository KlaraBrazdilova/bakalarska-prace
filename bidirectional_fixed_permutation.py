import numpy as np
from max_sub_array import max_sub_array

    
def bfp(M: np.matrix):
    W = M.copy()
    m, n = W.shape
    W[W == 1] = 1
    W[W == 0] = -1
    tosort = np.zeros((m, 2))

    for i in range(m):
        x = max_sub_array(W[i])
        tosort[i,0] = x[0]
        tosort[i,1] = x[1]       

    perm = np.argsort(tosort[:,0])
    perm2 = np.argsort(tosort[:,1])
    A = M[perm]
    return A


# M = np.matrix([[0, 0, 1, 1, 1], [0, 1, 0, 1, 0], [
#                      1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
# bfp(M)