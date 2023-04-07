import numpy as np
import copy
import matplotlib.pyplot as plt

from bidirectional_fixed_permutation import bfp

def spectral_ordering(M: np.matrix) -> np.matrix:
    [m, n] = M.shape
    M = M[np.random.permutation(m), :]
    M = M[:, np.random.permutation(n)]

    Q = np.array(copy.deepcopy(M))
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            # # Pearson's coeficient
            # pom = np.correlate(Q[:, i], Q[:, j])
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

    #Eigenvalues and eigenvectors
    V, D = np.linalg.eig(L) #eig just for square arrray, eigvals for general matrix

    #eigenvector

    #prepis z matlabu 
    # perm = np.sort(np.diag(D), kind='stable') #proc je tu diag?
    # column = V[perm[1]]
    # perm = np.sort(column, kind='stable')[::-1][n]
    # A = M[:, perm]

    a = np.argsort(V, kind='stable')
    perm = np.argsort(D[a[1]], kind='stable')
    column = V[perm]
    perm = np.argsort(column, kind='stable')[::-1][:n] #reverse order
    A = M[:, perm]


    return A
