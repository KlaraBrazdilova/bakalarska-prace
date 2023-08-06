import numpy as np
from matrix_similarity import matrix_similarity
from matrix_product_2 import matrix_product_2

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
