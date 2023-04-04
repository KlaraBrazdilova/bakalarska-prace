import numpy as np
import copy

M = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
                     1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0],  [0, 1, 0, 1, 1, 0]])

[m, n] = M.shape
M = M[np.random.permutation(m), :]
M = M[:, np.random.permutation(n)]
print(M)

#spectralcluster
Q = copy.deepcopy(M).transpose()
S = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        pom = np.correlate(np.array(Q[i])[0], np.array(Q[i])[0])
        S[i,j] = (1 + pom)/2 #Pearson's coeficient
        S[j,i] = (1 + pom)/2 #Pearson's coeficient

#Laplacian matrix
L = np.diag(np.diag(S)) - S
# print(L)
#Eigenvalues and eigenvectors
V, D = np.linalg.eig(L) #eig just for square arrray, eigvals for general matrix
# print(V)
# print(D)
#eigenvector
a = np.argsort(V)
b = a[1]
perm = np.argsort(D[b])

column = V[perm]
# print(column)
perm2 = np.argsort(column)[::-1][:n]
# print(perm2) 
# print(M.shape)
A = M[perm2]
print(A)

#radky k sobe pomoci max-sub array problem - co bude vyhodnejsi zmenit z 0 na 1 aby to bylo co nejlepší
