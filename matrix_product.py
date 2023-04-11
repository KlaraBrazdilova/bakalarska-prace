import numpy as np
from matrix_similarity import matrix_similarity

def matrix_product(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute the binary matrix product of A and B.
    Parameters
    ----------
    A : array_like, shape (M, K)
    B : array_like, shape (K, N)
    Returns
    -------
    C : array, shape (M, N)
    """
    # Check that A and B have compatible shapes
    if A.shape[1] != B.shape[0]:
        raise ValueError('matrix shapes are not aligned')
    
    # Create the result matrix
    C = np.zeros((A.shape[0], B.shape[1]), dtype=bool)

    # Compute the matrix product
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            # Compute the dot product of row i of A and column j of B
            dot_product = False
            for k in range(A.shape[1]):
                dot_product |= A[i, k] & B[k, j]
            C[i, j] = dot_product

    return C   

# A = np.loadtxt("data/zoo/grecond-alternating-A.csv",
#                  delimiter=",", dtype=int)
# B = np.loadtxt("data/zoo/grecond-alternating-B.csv",
#                  delimiter=",", dtype=int)
# I = np.loadtxt("data/zoo/zoo.csv", delimiter=",", dtype=int)
# A = np.matrix([[1, 0, 0, 1 ,0],[0,0,1,0,0], [0,1,0,0,0], [1,0,0,0,1], [1,0,0,0,0]])
# B = np.matrix([[0, 0, 0, 1, 1,0],[1,1,0,0,1,1], [0,1,0,1,0,1], [0,0,1,0,0,1], [1,0,0,0,0,0]])
# I = np.matrix([[0,0,1,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1],[1,0,0,1,1,0],[0,0,0,1,1,0]])
# product = matrix_product(A, B)
# print(product)
# print(matrix_similarity(product, I))

# def binary_matrix_product(A, B): #chatGPT
#     # ensure A and B are binary matrices
#     if not np.all(np.in1d(A, [0,1])) or not np.all(np.in1d(B, [0,1])):
#         raise ValueError("Input matrices must be binary")

#     # compute product using dot product and boolean operators
#     return (A.dot(B) > 0).astype(int)         