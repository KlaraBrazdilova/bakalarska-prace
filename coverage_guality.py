import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from matrix_similarity import matrix_similarity
from matrix_product import matrix_product

A = np.loadtxt("data/zoo/grecond-chat-A-alternating-deleted-band-30.csv",
                 delimiter=",", dtype=int)
B = np.loadtxt("data/zoo/grecond-chat-B-alternating-deleted-band-30.csv",
                 delimiter=",", dtype=int)
I = np.loadtxt("data/zoo/zoo.csv", delimiter=",", dtype=int)

product = matrix_product(A, B)
coverage = []
for i in range(I.shape[0]):
    coverage.append(matrix_similarity(product[0:i,:], I[0:i,:]))
        

fig, axs = plt.subplots(1, 1, figsize=(5, 5))
axs.plot(range(I.shape[0]), coverage)
plt.tight_layout()
plt.show()