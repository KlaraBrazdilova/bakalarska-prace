import numpy as np

def barycenter(M):
    [m, n] = M.shape
    indexes_cols = np.arange(1, n+1)
    indexes_rows = np.arange(1, m+1)
    A = M.copy()
    old = M.copy()
    trans = False
    while 1:
        cost = np.zeros(A.shape[0])

        for i in range(A.shape[0]):
            if trans:
                cost[i] = np.sum(np.multiply(A[i], indexes_rows)) / np.sum(A[i, :])
            else:
                cost[i] = np.sum(np.multiply(A[i], indexes_cols)) / np.sum(A[i, :])

        perm = np.argsort(cost)
        B = A[perm, :]

        if np.all(old == B):
            break

        A = B.transpose()
        old = A.copy()
        trans = not trans
        
    if trans:
        A = A.transpose()
    return A