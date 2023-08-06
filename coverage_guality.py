import numpy as np

from matrix_product_2 import matrix_product_2


def errors(product, I):
    error = 0
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if (I[i,j] == 1 and product[i,j] == 0) or (I[i,j] == 0 and product[i,j] == 1):
                error += 1
    return error                  

def coverage_guality_2(A, B, I):
    coverage = [] #pridat 0 na začátek
    for i in range(1, I.shape[0]):
        coverage.append(1 - errors(matrix_product_2(A[:,0:i], B[0:i,:]), I) / np.sum(I))
    return coverage

def simple_matching_coefficient(d, b):
    return np.sum(np.logical_and(d, b)) + np.sum(np.logical_and(np.logical_not(d), np.logical_not(b))) / b.size

def coverage_quality_smc(A, B, I_A,I_B):
    coverage = []
    for i in range(1, 10):
        coverage.append(simple_matching_coefficient(matrix_product_2(A[:,i-1:i], [B[i,:]]), matrix_product_2(I_A[:,i-1:i], [I_B[i,:]])))

    return coverage