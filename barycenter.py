import numpy as np

# M = np.random([0,1], 50, 40)
# M = np.matrix(M)
M = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
                     1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])

[m, n] = M.shape
indexes_cols = np.arange(1, n)
indexes_rows = np.arange(1, m)
A = M.copy()
old = M.copy()

while 1:
    cost = np.zeros(A.shape[0])

    # for i in range(A.shape[0]):
    #     # pom = np.vdot(A[i,:], [1, A.shape[1]]) / sum(A[i,:])
    #     # cost[i] = sum(pom)
    #     cost[i] = np.sum(A[i,:] * indexes[0:A.shape[1]]) / np.sum(A[i,:])
    
    for i in range(A.shape[0]):
        # pom = []
        # for j in range(A.shape[1]):
        #     pom.append(A[i,j] * indexes[i])
        print(indexes_rows.shape, indexes_cols.shape, A[i].shape)
        print(np.multiply(A[i], indexes_rows))
        cost[i] = np.sum(np.multiply(np.array(A[i])[0], indexes_rows[i])) / np.sum(A[i, :])
        print(cost[i])

        
    perm = np.argsort(cost)

    #[np.sort(cost, 'ascend'), np.perm]
    #perm = np.argsort(cost)
    B = A[perm, :]

    if np.all(old == B):
        break

    A = B.transpose()
    old = A.copy()

print(A)