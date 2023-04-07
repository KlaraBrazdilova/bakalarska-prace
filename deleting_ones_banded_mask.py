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

M = np.loadtxt("data/barycenter-zoo.csv",
                 delimiter=",", dtype=int)
vstup = copy.deepcopy(M)
A, C = banded_ones(M, 10)  

# newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ["blue", "yellow", "pink"])

viridis = cm.get_cmap('viridis', 256)
newcolors = viridis(np.linspace(0, 1, 256))
pink = np.array([248/256, 24/256, 148/256, 1])
newcolors[:25, :] = pink
newcmp = ListedColormap(newcolors)

fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp)
axs[0].set_title('Original')

axs[1].imshow(C, cmap=newcmp)
axs[1].set_title('Deleting')

axs[2].imshow(A, cmap=newcmp)
axs[2].set_title('banded-mask')

plt.show()