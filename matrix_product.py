import numpy as np
from matrix_similarity import matrix_similarity

def matrix_product(A: np.matrix, B: np.matrix) -> np.matrix:
    """Compute the binary matrix product of A and B.
    Parameters
    ----------
    A : array_like, shape (M, K)
    B : array_like, shape (K, N)
    Returns
    -------
    C : array, shape (M, N)
    """
    # Check that A and B have compatible shapes
    if A.shape[1] != B.shape[0]:
        raise ValueError('matrix shapes are not aligned')
    
    # Create the result matrix
    C = np.zeros((A.shape[0], B.shape[1]), dtype=bool)

    # Compute the matrix product
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            # Compute the dot product of row i of A and column j of B
            dot_product = False
            for k in range(A.shape[1]):
                dot_product |= A[i, k] & B[k, j]
            C[i, j] = dot_product

    return C   

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating", "spectral-ordering-pearson-bfp-fix"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("deleted-band", ["30", "50", "70", "90"])]
folders = ["healthcare"] #"mushroom" export zvlast kvuli roztazeni , "paleo", "zoo", "healthcare"

for folder in folders:
    for type in types:
        for filter in filters:
            filter_name, filter_amount = filter
            for amount in filter_amount:
                A = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-A.csv", delimiter=",", dtype=int)
                B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-B.csv", delimiter=",", dtype=int)
                
                product = matrix_product(A, B)
                np.savetxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-product.csv", product, delimiter=",", fmt="%d")
                print(amount)