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
                final[i,j] = 0 

    return final