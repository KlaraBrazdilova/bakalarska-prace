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
bary = barycenter(M)
banded = bfp(bary)
print("done")
A, B, factors = GreConD(banded)
#product = matrix_product(A, B)
#sim = matrix_similarity(product, banded)
# print(factors)

# newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "black"])
# fig, axs = plt.subplots(1, 4, figsize=(15, 10))
# axs[0].imshow(vstup, cmap=newcmp)
# axs[0].set_title('Original')

# axs[1].imshow(banded, cmap=newcmp)
# axs[1].set_title('Alternating - BFP')

# axs[2].imshow(A, cmap=newcmp)
# axs[2].set_title('GreConD - A')

# axs[3].imshow(B, cmap=newcmp)
# axs[3].set_title('GreConD - B')

# plt.show()
np.savetxt("data/zoo/barycenter-chat.csv", banded, delimiter=",")
np.savetxt("data/zoo/grecond-barycenter-chat-A.csv", A, delimiter=",")
np.savetxt("data/zoo/grecond-barycenter-chat-B.csv", B, delimiter=",")
print(factors)
