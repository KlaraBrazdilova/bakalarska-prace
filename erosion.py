import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import math


def erosion(matrix, mask):
    matrix_copy = matrix.copy()
    m, n = matrix.shape
    mask_m, mask_n = mask.shape
    size = math.floor(mask_m/2)
    # mask_ones = np.count_nonzero(mask)
    mask_ones = 5
    for i in range(m):
        for j in range(n):

            count = 0
            for k in range(mask_m):
                for l in range(mask_n):
                    try:
                        if mask[k, l] and not matrix[i-size+k, j-size+l]:                        
                            matrix_copy[i, j] = 0
                            break
                        else:
                            count += 1
                    except IndexError:
                        pass

            if count == mask_ones:
                matrix_copy[i, j] = 1  

    return matrix_copy 

# M = np.loadtxt('data/paleo/spectral-ordering-pearson-bfp-diletation.csv', delimiter=',', dtype=int)
# vstup = M.copy()
# mask = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# filter = erosion(M, mask)
# # print(M)
# newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue', 'green'])
# newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].imshow(vstup, cmap=newcmp_black_white)
# axs[0].set_title('Original')
# axs[1].imshow(filter, cmap=newcmp_black_white)
# axs[1].set_title('filter, 3, 0.7')
# plt.show()         
# np.savetxt("data/paleo/spectra-ordering-pearson-bfp-diletation-erosion.csv", filter, delimiter=",")        