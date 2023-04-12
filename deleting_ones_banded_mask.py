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
                final[i,j] = 0.1
    return band, final

M = np.loadtxt("data/zoo/alternating.csv",
                 delimiter=",", dtype=int)
vstup = copy.deepcopy(M)
band, deleted = banded_ones(M, 50)  

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0, 'white'), (0.1, 'blue'), (1,'black')])

fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp)
axs[0].set_title('Original')

axs[1].imshow(band, cmap=newcmp)
axs[1].set_title('Band')

axs[2].imshow(deleted, cmap=newcmp)
axs[2].set_title('Deleting')


plt.show()