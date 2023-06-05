from math import floor
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

def square_count(M, size, i, j):
    """Count number of 1s in square of size size around (i,j)."""
    count = 0
    max = floor(size/2)
    for k in range(max+1):
        for l in range(max+1):
            try:
                if M[i + k, j + l]:
                    count += 1
                if M[i - k, j - l]:
                    count += 1 
            except IndexError:
                pass    
    count -= M[i, j]                            
    return count/(size*size)


def square_filter(size, M, limit):
    """Filter matrix with square filter of size size."""
    N = M.copy()
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if square_count(M, size, i, j) > limit:
                N[i, j] = 1
            else:
                N[i, j] = 0
    return N


M = np.loadtxt('data/paleo/barycenter-bfp.csv', delimiter=',', dtype=int)
vstup = M.copy()
M = square_filter(3, M, 0.5)
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')
axs[1].imshow(M, cmap=newcmp_black_white)
axs[1].set_title('filter, 3, 1')
plt.show()