import numpy as np

B = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1]])
[m, n] = B.shape
indexes_rows = np.arange(m)
indexes_cols = np.arange(n)
print(indexes_cols)
for i in range(B.shape[0]):
    print(indexes_cols.shape, B[i].shape)
    print(np.multiply(B[i], indexes_cols))