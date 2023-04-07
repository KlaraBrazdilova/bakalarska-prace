import numpy as np
import copy
import matplotlib.pyplot as plt

from bidirectional_fixed_permutation import bfp

def spectral_ordering(M: np.matrix) -> np.matrix:
    [m, n] = M.shape

    Q = np.array(copy.deepcopy(M))
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            # Pearson's coeficient
            # pom = np.corrcoef(Q[:, i], Q[:, j])[0][1]
            # S[i,j] = (1 + pom)/2 
            # S[j,i] = (1 + pom)/2 
            
            # Jaccard's coeficient
            x = Q[:,i]
            y = Q[:,j]
            union = sum(x) + sum(y)
            intersection = 0
            for k in range(m):
                if x[k] and y[k]:
                    intersection += 1
            S[i,j] = intersection / union
            S[j,i] = intersection / union

    #Laplacian matrix
    L = np.diag(np.diag(S)) - S

    # Eigenvalues and eigenvectors
    D, V = np.linalg.eigh(L)
    
    a = np.argsort(D) 
    perm = np.argsort(V[:,a[1]], kind='stable')
    A = M[:, perm]

    return A