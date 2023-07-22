import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from matrix_similarity import matrix_similarity
from matrix_product import matrix_product

def coverage_guality(A, B, I):
    coverage = [] #pridat 0 na začátek
    for i in range(1, I.shape[0]):
        coverage.append(matrix_similarity(matrix_product(A[:,0:i], B[0:i,:]), I))
    return coverage

# def coverage_guality_2(product, I):
#     coverage = [] #pridat 0 na začátek
#     for i in range(1, I.shape[0]):
#         coverage.append(matrix_similarity(product, I))
#     return coverage

# A = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-A.csv",
#                              delimiter=",", dtype=int)
# B = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-B.csv",
#                              delimiter=",", dtype=int)
# I = np.loadtxt("data/healthcare/alternating/square-filter/alternating-square-filter-0.3.csv", delimiter=",", dtype=int)
# product = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-product.csv", 
#                      delimiter=",", dtype=int)
# print("nacteno")
# print(coverage_guality_2(product,I))
# print(coverage_guality(A,B,I))