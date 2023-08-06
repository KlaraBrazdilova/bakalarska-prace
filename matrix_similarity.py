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
    print(X)
    print(Z)
    print(Y)
    result = 100 * X/Y
    if result > 100:
        result = 100 * X/Z
    return result

def jaccard_similarity(matrix1, matrix2):
    intersection = np.logical_and(matrix1, matrix2).sum()
    union = np.logical_or(matrix1, matrix2).sum()
    return intersection / union

def percentage_similarity(matrix1, matrix2):
    jaccard_sim = jaccard_similarity(matrix1, matrix2)
    return jaccard_sim * 100

def simple_matching_coefficient(matrix1, matrix2):
    # Vypočítáme počet shodných prvků (0 i 1) mezi maticemi
    matching_elements = np.sum(matrix1 == matrix2)
    
    # Vypočítáme celkový počet prvků ve dvou maticích
    total_elements = matrix1.size
    
    # Výpočet Simple Matching Coefficient
    smc = matching_elements / total_elements
    return smc*100# - procenta verze

# M = np.loadtxt("data/zoo/spectral-ordering-pearson-bfp/square-filter/spectral-ordering-pearson-bfp-square-filter-0.3.csv",
#                  delimiter=",", dtype=int)
# A = np.loadtxt("data/zoo/spectral-ordering-pearson-bfp/spectral-ordering-pearson-bfp.csv",
#                  delimiter=",", dtype=int)

# print(percentage_similarity(M, A))
# print(simple_matching_coefficient(M, A))
# print(matrix_similarity(M, A))
# print(matrix_similarity(A, M))