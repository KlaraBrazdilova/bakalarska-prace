import numpy as np
from matrix_product import matrix_product

def matrix_similarity(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute coverage quality of matrix A and matrix B."""
    
    sum1 = np.sum(A-B)
    sum2 = np.sum(A)
    similarity = sum1/sum2
    return similarity

# matrix_test = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
#                      1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])    
# matrix_test2 = np.matrix([[0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 0], [
#                      1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0]])
# print(matrix_similarity(matrix_test, matrix_test2))