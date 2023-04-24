import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import math


def diletation(matrix, mask):
    m, n = matrix.shape
    mask_m, mask_n = mask.shape
    size = math.floor(mask_m/2)
    for i in range(m):
        for j in range(n):

            for k in range(mask_m):
                for l in range(mask_n):
                    try:
                        if mask[k, l] and matrix[i-size+k, j-size+l]:
                            matrix[i, j] = 1
                            break
                    except IndexError:
                        pass
    return matrix                    

M = np.loadtxt('data/paleo/spectra-ordering-pearson-bfp.csv', delimiter=',', dtype=int)
vstup = M.copy()
mask = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
filter = diletation(M, mask)
# print(M)
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue', 'green'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')
axs[1].imshow(filter, cmap=newcmp_black_white)
axs[1].set_title('diletation')
plt.show()