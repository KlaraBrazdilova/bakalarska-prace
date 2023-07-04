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
            # pom = np.corrcoef(Q[:, i], Q[:, j])[0][1]
            # S[i,j] = (1 + pom)/2 
            # S[j,i] = (1 + pom)/2 
            
            # Jaccard's coeficient
            x = Q[:,i]
            y = Q[:,j]
            
            intersection = 0
            for k in range(m):
                if x[k] and y[k]:
                    intersection += 1

            union = sum(x) + sum(y) - intersection  
                  
            S[i,j] = intersection / union
            S[j,i] = intersection / union

    #Laplacian matrix
    L = np.diag(np.diag(S)) - S

    # Eigenvalues and eigenvectors
    D, V = np.linalg.eigh(L)
    
    a = np.argsort(D) 
    perm = np.flip(np.argsort(V[:,a[1]], kind='stable'))
    A = M[:, perm]

    return A

# slozky = ["paleo","zoo", "healthcare", "mushroom"]
# typy = ["spectral-ordering-pearson-bfp","barycenter-bfp","alternating"]
M = np.loadtxt("data/zoo/zoo.csv",
                            delimiter=",", dtype=int)
# M = np.array([[0, 0, 1, 0],[1, 1, 1, 1], [0, 1, 1, 1],[0, 1, 1, 0]])
vysledek = bfp(spectral_ordering(M))

print(vysledek)
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
axs.imshow(vysledek, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
axs.set_title("spectral")
plt.show()
# np.savetxt("data/paleo/paleo-spectral-ordering-jaccard.csv", vysledek, delimiter=",", fmt='%d')