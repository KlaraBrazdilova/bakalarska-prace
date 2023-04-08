import copy
import numpy as np
import matplotlib.pyplot as plt

from grecond import GreConD
from barycenter import barycenter
from matrix_similarity import matrix_similarity
from matrix_product import matrix_product
from bidirectional_fixed_permutation import bfp
from alternating import alternating
from spectral_ordering import spectral_ordering
from simple_sort import simple_sort


M = np.loadtxt("data/zoo.csv",
                 delimiter=",", dtype=int)
# vstup = copy.deepcopy(M)


vstup = copy.deepcopy(M)
bary = spectral_ordering(M)
banded = bfp(bary)

# vstup = copy.deepcopy(M)
# bary = spectral_ordering(M)
# banded = bfp(bary)
# A, B, factors = GreConD(banded)
#product = matrix_product(A, B)
#sim = matrix_similarity(product, banded)
# print(factors)

fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(~vstup, cmap='gray')
axs[0].set_title('Original')

axs[1].imshow(~bary, cmap='gray')
axs[1].set_title('Spectral Pearson')

axs[2].imshow(~banded, cmap='gray')
axs[2].set_title('Banded - BFP')

plt.show()
# np.savetxt("data/spectral-jaccard-zoo.csv", bary, delimiter=",")