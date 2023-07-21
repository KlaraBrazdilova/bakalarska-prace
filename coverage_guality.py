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
