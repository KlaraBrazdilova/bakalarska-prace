import numpy as np
import copy


def spectral_ordering(M: np.matrix) -> np.matrix:
    """
    Spetral ordering method for finding a good column permutation of a matrix for algorithm BFP.

    Input: binary matrix M
    Output: binary matrix M with a good column permutation
    """
    
    [m, n] = M.shape

    Q = np.array(copy.deepcopy(M))
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            # # Pearson's coeficient
            pom = np.corrcoef(Q[:, i], Q[:, j])[0][1]
            S[i,j] = (1 + pom)/2
            S[j,i] = (1 + pom)/2

    # Laplacian matrix
    L = np.diag(np.diag(sum(S,2))) - S

    # Eigenvalues and eigenvectors
    D, V = np.linalg.eigh(L)

    a = np.argsort(D)
    perm = np.flip(np.argsort(V[:, a[1]], kind="stable"))
    A = M[:, perm]

    return A