import numpy as np

def matrix_product_2(A: np.matrix, B: np.matrix) -> np.matrix:
    product = np.matmul(A, B) 

    for i in range(product.shape[0]):
        for j in range(product.shape[1]):
            if product[i,j] > 0:
                product[i,j] = 1
               
    return product
