import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, pyplot as plt
from matplotlib.colors import ListedColormap
import copy


def banded_matrix(n: int, m: int) -> np.matrix:
    """Create a banded matrix with n rows and m columns."""    
    B = np.zeros((n, m))
    transpo = False
    if m > n:
        B = B.transpose() #trasnponovani pomale, ale je to jednodussi
        transpo = True
    height = B.shape[0]
    width = B.shape[1]            
    size = int(np.round(height/width))
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

def banded_distance(M: np.matrix, k: int) -> np.matrix:
    m,n = M.shape
    band = banded_matrix(m, n)
    size = int(np.round(n * (100-k) / 100))
    change = False
    for i in range(m): #radek
        for j in range(n): #sloupec
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

# M = np.loadtxt("data/barycenter-zoo.csv",
#                  delimiter=",", dtype=int)

# vstup = copy.deepcopy(M)
# C = banded_matrix(M.shape[0], M.shape[1]) 
# A = banded_distance(M, 5) 

# viridis = cm.get_cmap('viridis', 256)
# newcolors = viridis(np.linspace(0, 1, 256))
# pink = np.array([248/256, 24/256, 148/256, 1])
# newcolors[:25, :] = pink
# newcmp = ListedColormap(newcolors)

# fig, axs = plt.subplots(1, 3, figsize=(10, 5))
# axs[0].imshow(vstup, cmap=newcmp)
# axs[0].set_title('Original')

# axs[1].imshow(C, cmap=newcmp)
# axs[1].set_title('banded-mask')

# axs[2].imshow(A, cmap=newcmp)
# axs[2].set_title('banded-distance')

# plt.show()