import numpy as np
from max_sub_array import max_sub_array

M = np.zeros(12,10)

M = np.matrix(M)

A = M
no_of_iterations = 20

for i in range(no_of_iterations):
    [m,n] = A.shape
    W = A

    for i in W:
        if i == 0:
            i = -1

    tosort = []

    for i in range(m):
        x = max_sub_array(W[i,:])
        tosort[i,0] = x(0)
        tosort[i,1] = x(1)

    [np.sort(tosort), np.perm]
    A = A[np.perm, :]
    A = A[:, np.perm]