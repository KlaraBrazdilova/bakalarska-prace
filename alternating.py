import numpy as np

from max_sub_array import max_sub_array


def alternating(M: np.matrix):
    """
    Althernating method for sorting rows and columns of a matrix to banded structure.¨
    
    Input: binary matrix M 
    Output: banded binary matrix M
    """

    A = M
    no_of_iterations = 20

    for i in range(no_of_iterations):
        m, n = A.shape

        W = A.copy()
        W[W == 1] = 1
        W[W == 0] = -1
        tosort = np.zeros((m, 2))

        # compute max subarray
        for i in range(m):
            x = max_sub_array(W[i])
            tosort[i,0] = x[0]
            tosort[i,1] = x[1]       

        # sort rows
        perm = np.lexsort((tosort[:, 1], tosort[:, 0]))
        A = A[perm, :]
        A = A.transpose()

    return A    