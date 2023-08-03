import numpy as np

def matrix_similarity(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute coverage quality of matrix A and matrix B."""
    
    sum1 = np.sum(np.bitwise_xor(A,B))
    sum2 = np.sum(np.abs(A))
    # print(sum1/sum2)
    similarity = 1 - sum1/sum2

    return similarity

def similarity_2(A, B):
    Y = np.sum(A)
    Z = np.sum(B)
    X = np.sum(np.logical_xor(A, B))
    result = 100 * X/Y
    if result > 100:
        result = 100 * X/Z
    return result


M = np.loadtxt("data/paleo/spectral-ordering-pearson-bfp/square-filter/spectral-ordering-pearson-bfp-square-filter-0.3.csv",
                 delimiter=",", dtype=int)
A = np.loadtxt("data/paleo/spectral-ordering-pearson-bfp/spectral-ordering-pearson-bfp.csv",
                 delimiter=",", dtype=int)

print(similarity_2(A,M))
# print(matrix_similarity(M, A))
# print(matrix_similarity(A, M))