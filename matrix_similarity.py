import numpy as np

def matrix_similarity(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute coverage quality of matrix A and matrix B."""
    
    sum1 = np.sum(np.abs(np.bitwise_xor(A,B))) 
    sum2 = np.sum(np.abs(A))
    similarity = 1 - sum1/sum2

    return similarity


M = np.loadtxt("data/zoo/alternating.csv",
                 delimiter=",", dtype=int)
A = np.loadtxt("data/zoo/alternating-bfp.csv",
                 delimiter=",", dtype=int)

print(matrix_similarity(M, A))