from matplotlib import pyplot as plt
import numpy as np
import copy
from banded_matrix import banded_matrix

def banded_ones(M: np.matrix, k: int) -> np.matrix:
    """Return a matrix M withnout a 1s around diagonal in distance k(%)."""
    final = copy.deepcopy(M)
    band = banded_matrix(M.shape[0], M.shape[1])
    print(band)
    size = k
    for i in range(M.shape[0]): #radek
        for j in range(M.shape[1]): #sloupec
            if j + 1 != M.shape[1] and band[i, j] and not band[i, j + 1]:
                if j + size + 1 > M.shape[1]:
                    end = M.shape[1]
                else:
                    end = size + 1    
                for k in range(j, end):
                    band[i, k] = 1
            if band [i, j] and not band[i, j - 1]:
                if j - size - 1< 0:
                    end = -1
                else:
                    end = j - size  - 1  
                for k in range(j, end, -1):
                    band[i, k] = 1        
    print(band)    
    for i in range(final.shape[0]):
        for j in range(final.shape[1]):
            final[i,j] *= band[i,j]
    print(final)        
    return final

M = np.loadtxt("data/barycenter-zoo.csv",
                 delimiter=",", dtype=int)
vstup = copy.deepcopy(M)
C = banded_ones(M, 10)  
for i in range(C.shape[0]):
    print(C[i])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(~vstup, cmap='gray')
axs[0].set_title('Original')

axs[1].imshow(~C, cmap='gray')
axs[1].set_title('Deleting')

plt.show()