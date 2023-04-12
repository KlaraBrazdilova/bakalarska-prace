import copy
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from grecond_chatgpt import GreConD
from barycenter import barycenter
from matrix_similarity import matrix_similarity
from matrix_product import matrix_product
from bidirectional_fixed_permutation import bfp
from alternating import alternating
from spectral_ordering import spectral_ordering
from simple_sort import simple_sort


M = np.loadtxt("data/zoo/zoo.csv",
                 delimiter=",", dtype=int)


vstup = copy.deepcopy(M)
bary = spectral_ordering(M)
banded = bfp(bary)
print("done")
# A, B, factors = GreConD(banded)
#product = matrix_product(A, B)
#sim = matrix_similarity(product, banded)
# print(factors)

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "black"])
fig, axs = plt.subplots(1, 3, figsize=(15, 10))
axs[0].imshow(vstup, cmap=newcmp)
axs[0].set_title('Original')

axs[1].imshow(bary, cmap=newcmp)
axs[1].set_title('Spectral Ordering - Pearson s coeficient')

axs[2].imshow(banded, cmap=newcmp)
axs[2].set_title('BFP')

# axs[3].imshow(B, cmap=newcmp)
# axs[3].set_title('GreConD - B')

plt.show()
np.savetxt("data/zoo/spectra-ordering-pearson.csv", bary, delimiter=",")
np.savetxt("data/zoo/spectra-ordering-pearson-bfp.csv", banded, delimiter=",")
# print(factors)
