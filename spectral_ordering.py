import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib

from bidirectional_fixed_permutation import bfp


def spectral_ordering(M: np.matrix) -> np.matrix:
    [m, n] = M.shape

    Q = np.array(copy.deepcopy(M))
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            # # Pearson's coeficient
            pom = np.corrcoef(Q[:, i], Q[:, j])[0][1]
            S[i,j] = (1 + pom)/2
            S[j,i] = (1 + pom)/2

            # Jaccard's coeficient
            # coef = sum(np.bitwise_and(Q[:, i], Q[:, j])) / sum(
            #     np.bitwise_or(Q[:, i], Q[:, j])
            # )
            # S[i, j] = (1 + coef) / 2
            # S[j, i] = S[i, j]

    # Laplacian matrix
    L = np.diag(np.diag(sum(S,2))) - S

    # Eigenvalues and eigenvectors
    D, V = np.linalg.eigh(L)

    a = np.argsort(D)
    perm = np.flip(np.argsort(V[:, a[1]], kind="stable"))
    A = M[:, perm]

    return A

newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list(
    "", ["white", "black"]
)
files = ["paleo","zoo", "healthcare", "mushroom"]
# typy = ["spectral-ordering-pearson-bfp","barycenter-bfp","alternating"]
for file in files:
    M = np.loadtxt("data/"+file+"/"+file+".csv", delimiter=",", dtype=int)
    spectral = spectral_ordering(M)
    vysledek = bfp(spectral)
    np.savetxt("data/"+file+"/spectral-ordering-pearson-bfp-fix.csv", vysledek, delimiter=",", fmt='%d')
    np.savetxt("data/"+file+"/spectral-ordering-pearson-fix.csv", spectral, delimiter=",", fmt='%d')
    fig, axs = plt.subplots(1, 1, figsize=(12, 9))
    axs.imshow(vysledek, cmap=newcmp_black_white)  # pro mushroom aspect='auto', interpolation='nearest'
    axs.set_title("spectral ordering - pearson coeficient")
    plt.savefig("data/"+file+"/spectral-ordering-pearson-bfp-fix.png")
    matplotlib.pyplot.close()
    # plt.show()
# M = np.loadtxt("data/paleo/paleo.csv", delimiter=",", dtype=int)


# print(vysledek)

# fig, axs = plt.subplots(1, 1, figsize=(12, 9))
# axs.imshow(
#     vysledek, cmap=newcmp_black_white
# )  # pro mushroom aspect='auto', interpolation='nearest'
# axs.set_title("spectral ordering - pearson coeficient")
# plt.show()
# np.savetxt("data/paleo/paleo-spectral-ordering-jaccard.csv", vysledek, delimiter=",", fmt='%d')
