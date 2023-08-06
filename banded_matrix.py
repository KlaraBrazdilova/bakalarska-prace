import numpy as np


def banded_matrix(n: int, m: int) -> np.matrix:
    """Create a banded matrix with n rows and m columns. Band is like main diagonal. """ 

    B = np.zeros((n, m))
    transpo = False

    if m > n:
        B = B.transpose()
        transpo = True

    height = B.shape[0]
    width = B.shape[1]            
    size = int(np.round(height/width))

    for j in range(width): 
        index = j*size

        if index + size >= height:
            end = height
        else:
            end = index + size + 1 

        for i in range(index, end): 
            B[i, j] = 1

    if transpo:
        B = B.transpose()

    return np.matrix(B)

def banded_distance(M: np.matrix, k: int) -> np.matrix:
    """
    Create a banded matrix. Band is width k % of the matrix.

    Input: binary matrix M, integer k
    Output: banded binary matrix A
    """

    m,n = M.shape
    band = banded_matrix(m, n)
    size = int(np.round(n * (100-k) / 100))
    change = False

    for i in range(m):
        for j in range(n): 
            if j + 1 != n and band[i, j] and not band[i, j + 1]:
                if j + size + 1 > n:
                    end = n
                else:
                    end = j + size + 1 

                for k in range(j, end):
                    band[i, k] = 1

                change = True

            if band [i, j] and not band[i, j - 1]:
                if j - size - 1< 0:
                    end = -1
                else:
                    end = j - size  - 1  

                for k in range(j, end, -1):
                    band[i, k] = 1      

            if change:
                break;
        
        change = False       
                  
    return band