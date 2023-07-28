import numpy as np

def matrix_product_2(A: np.matrix, B: np.matrix) -> np.matrix:
    product = np.matmul(A, B) 
    # print(product)
    for i in range(product.shape[0]):
        for j in range(product.shape[1]):
            if product[i,j] > 0:
                product[i,j] = 1
    # print(product)            
    return product

# A = np.loadtxt("data/mushroom/alternating/diletation-erosion/GreConD/alternating-diletation-erosion-col-matrix-3x2-grecond-A.csv", delimiter=",", dtype=int)
# B = np.loadtxt("data/mushroom/alternating/diletation-erosion/GreConD/alternating-diletation-erosion-col-matrix-3x2-grecond-B.csv", delimiter=",", dtype=int)
# product = matrix_product_2(A, B)