import numpy as np
import copy
from bidirectional_fixed_permutation import bfp

def spectral_ordering(M: np.matrix) -> np.matrix:
    [m, n] = M.shape
    M = M[np.random.permutation(m), :]
    M = M[:, np.random.permutation(n)]

    Q = np.array(copy.deepcopy(M))
    print(Q)
    S = np.zeros((n, n))
    # print(n)
    for i in range(n):
        # print(i)
        for j in range(i, n):
            # print(j)
            #print(Q[:,i], Q[:,j])
            #pom = np.correlate(np.array(Q[:, i])[0], np.array(Q[:, j])[0]) #Pearson's coeficient
            union = np.union1d(Q[:,i], Q[:,j])
            intersection = np.intersect1d(Q[:,i], Q[:,j])
            S[i,j] = union.size/intersection.size #Jaccard's coeficient
            S[j,i] = union.size/intersection.size #Jaccard's coeficient
            # S[i,j] = (1 + pom)/2 #Pearson's coeficient
            # S[j,i] = (1 + pom)/2 #Pearson's coeficient

    #Laplacian matrix
    L = np.diag(np.diag(S)) - S

    #Eigenvalues and eigenvectors
    V, D = np.linalg.eig(L) #eig just for square arrray, eigvals for general matrix

    #eigenvector
    a = np.argsort(V)
    b = a[1]
    perm = np.argsort(D[b])
   
    column = V[perm]
    
    perm2 = np.argsort(column)[::-1][:n]
    
    A = M[:, perm2]
    print(A)
    C = bfp(A)
    #radky k sobe pomoci max-sub array problem - co bude vyhodnejsi zmenit z 0 na 1 aby to bylo co nejlepší
    print(C)
    return C

M = np.matrix([[0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [
                     1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0]])    
spectral_ordering(M)