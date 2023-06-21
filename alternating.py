import numpy as np
from max_sub_array import max_sub_array

def alternating(M: np.matrix):
    M = M[:, np.random.permutation(M.shape[1])]
    M = M[np.random.permutation(M.shape[0]), :]
    A = M
    no_of_iterations = 20

    for i in range(no_of_iterations):
        # utřídím řádky, transponuji matici a opakuji
        m, n = A.shape

        W = A.copy()
        W[W == 1] = 1
        W[W == 0] = -1
        tosort = np.zeros((m, 2))

        for i in range(m):
            x = max_sub_array(W[i])
            tosort[i,0] = x[0]
            tosort[i,1] = x[1]       

        perm = np.lexsort((tosort[:, 1], tosort[:, 0]))
        A = A[perm, :]
        A = A.transpose()
    return A    