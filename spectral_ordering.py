import numpy as np

M = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
                     1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])

[m, n] = M.shape
M = M[np.random.permutation(m), :]
M = M[:, np.random.permutation(n)]

#spectralcluster
Q = M.transpose()
S = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        pom = np.correlate(np.array(Q[i])[0], np.array(Q[i])[0])
        S[i,j] = (1 + pom)/2 #Pearson's coeficient
        S[j,i] = (1 + pom)/2 #Pearson's coeficient

#Laplacian matrix
L = np.diag(np.diag(S)) - S
print(L)
#Eigenvalues and eigenvectors
V, D = np.linalg.eig(L) #eig just for square arrray, eigvals for general matrix
print(D)
print(V)

#eigenvector
a = np.sort(V)
b = a[-1]
perm = np.sort(np.array(D[b])[0]) #chyba

column = V[:, perm]

#Fiedler's vector
# column = V[:, 1]
# perm = np.sort(column, 'descend')
# A = M[:, perm]

#simple sorting
# tosort = []
# for i in range(m):
#     tosort.append(np.argwhere(A[i, :] == 1)[0])
#     tosort.append(np.argwhere(A[i, :] == 1)[-1])

# print(A)
# print(tosort)
