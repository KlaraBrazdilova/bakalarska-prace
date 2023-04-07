import numpy as np
import copy


def banded_matrix(n: int, m: int) -> np.matrix:
    """Create a banded matrix with n rows and m columns."""    
    B = np.zeros((n, m))
    transpo = False
    if m > n:
        B = B.transpose() #trasnponovai pomale, ale je to jednodussi
        transpo = True
    height = B.shape[0]
    width = B.shape[1]            
    size = int(np.ceil(height/width))
    for j in range(width):    #sloupec
        index = j*size
        if index + size >= height:
            end = height
        else:
            end = index + size + 1 
        for i in range(index, end): #radek
            B[i, j] = 1
    if transpo:
        B = B.transpose()
    return np.matrix(B)

print(banded_matrix(5, 10))
