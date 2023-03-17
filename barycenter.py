import numpy as np

M = np.random([0,1], 50, 40)
M = np.matrix(M)

m = M.shape[0]
n = M.shape[1]
A = M
old = M

while 1:
    cost = np.zeros(A.shape[0], 1)
    for i in range(A.shape[0]):
        pom = np.vdot(A[i,:], [1, A.shape[1]]) / sum(A[i,:])
        cost[i] = sum(pom)

    [np.sort(cost, 'ascend'), np.perm]
    B = A[np.perm, :]

    if all(all(old == B)):
        break

    A = B
    old = A    

print(A)