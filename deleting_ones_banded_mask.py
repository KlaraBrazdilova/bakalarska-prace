from matplotlib import cm, pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap
import numpy as np
import copy
from banded_matrix import banded_matrix, banded_distance

def banded_ones(M: np.matrix, k: int) -> np.matrix:
    """Return a matrix M withnout a 1s around diagonal in distance k(%)."""
    final = copy.deepcopy(M)
    band = banded_distance(M, k)
    for i in range(final.shape[0]):
        for j in range(final.shape[1]):
            if not band[i,j] and final[i,j]:
                final[i,j] = 2
    return band, final

M = np.loadtxt("data/zoo/barycenter.csv",
                 delimiter=",", dtype=int)
vstup = copy.deepcopy(M)
A, C = banded_ones(M, 10)  

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "black", "deepskyblue"])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp)
axs[0].set_title('Original')

axs[1].imshow(C, cmap=newcmp)
axs[1].set_title('Deleting')


plt.show()