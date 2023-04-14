import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from matrix_similarity import matrix_similarity
from matrix_product import matrix_product

A = np.loadtxt("data/zoo/grecond-chat-A-alternating-deleted-band-30.csv",
                 delimiter=",", dtype=int)
B = np.loadtxt("data/zoo/grecond-chat-B-alternating-deleted-band-30.csv",
                 delimiter=",", dtype=int)
I = np.loadtxt("data/zoo/alternating.csv", delimiter=",", dtype=int)

# product = matrix_product(A, B)
coverage = [0] #pridat 0 na začátek
for i in range(1, I.shape[0]):
    coverage.append(matrix_similarity(matrix_product(A[:,0:i], B[0:i,:]), I))
        
print(coverage)
print(range(0,I.shape[0]))
fig, axs = plt.subplots(1, 1, figsize=(5, 5))
axs.plot(range(0,I.shape[0]), coverage)
plt.tight_layout()
plt.show()