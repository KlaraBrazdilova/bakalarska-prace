import numpy as np

def simple_sort(M:np.matrix):
    tosort = np.zeros((M.shape[0], 2))
    m, n = M.shape
    for i in range(M.shape[0]):
        tosort[i,0] = np.argsort(np.array(M[i])[0])[0]
        tosort[i,1] = np.argsort(np.array(M[i])[0])[n-1]

    perm = np.lexsort((tosort[:,0], tosort[:,1]))
    A = M[perm]    
    return A

