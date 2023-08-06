import numpy as np

def matrix_similarity(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute coverage quality of matrix A and matrix B."""
    
    sum1 = np.sum(np.bitwise_xor(A,B))
    sum2 = np.sum(np.abs(A))
    # print(sum1/sum2)
    similarity = 1 - sum1/sum2

    return similarity


def simple_matching_coefficient(matrix1, matrix2):
    # Vypočítáme počet shodných prvků (0 i 1) mezi maticemi
    matching_elements = np.sum(matrix1 == matrix2)
    
    # Vypočítáme celkový počet prvků ve dvou maticích
    total_elements = matrix1.size
    
    # Výpočet Simple Matching Coefficient
    similarity = matching_elements / total_elements
    return similarity*100 # - procenta verze
