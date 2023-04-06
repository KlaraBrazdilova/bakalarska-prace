import numpy as np

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
    C = np.zeros((A.shape[0], B.shape[1]))

    # Compute the matrix product
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                if A[i, k] and B[k, j]:
                    C[i, j] = 1

    return C            