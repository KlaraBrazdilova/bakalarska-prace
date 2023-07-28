import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matrix_similarity import matrix_similarity

print("Ahoj")

# def matrix_product_coverage(A: np.matrix, B: np.matrix) -> np.matrix:
#     """Compute the binary matrix product of A and B.
#     Parameters
#     ----------
#     A : array_like, shape (M, K)
#     B : array_like, shape (K, N)
#     Returns
#     -------
#     C : array, shape (M, N)
#     """
#     # Check that A and B have compatible shapes
#     if A.shape[1] != B.shape[0]:
#         raise ValueError('matrix shapes are not aligned')
    
#     # Create the result matrix
#     C = np.zeros((A.shape[0], B.shape[1]), dtype=bool)

#     # Compute the matrix product
#     for i in range(A.shape[0]):
#         for j in range(B.shape[1]):
#             # Compute the dot product of row i of A and column j of B
#             dot_product = False
#             for k in range(A.shape[1]):
#                 dot_product |= A[i, k] & B[k, j] #tady se to pokaždé liší 
#             C[i, j] = dot_product

#     return C 

# A = np.loadtxt("bakalarska-prace/data/zoo/grecond-chat-A.csv", delimiter=",", dtype=int)
# B = np.loadtxt("bakalarska-prace/data/zoo/grecond-chat-B.csv", delimiter=",", dtype=int)
# I = np.loadtxt("bakalarska-prace/data/zoo/zoo.csv", delimiter=",", dtype=int)
# zero = matrix_product_coverage(A[:,0:0], B[0:0,:])
# print(zero.shape)
# one = matrix_product_coverage(A[:,0:1], B[0:1,:])
# print(one.shape)
# two = matrix_product_coverage(A[:,0:2], B[0:2,:])
# print(two.shape)
# fig, axs = plt.subplots(1, 3, figsize=(12, 9)) 
# plt.tight_layout()
# newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

# axs[0].imshow(zero, cmap=newcmp_black_white)
# axs[1].imshow(one, cmap=newcmp_black_white)
# axs[2].imshow(two, cmap=newcmp_black_white)
# plt.show()
