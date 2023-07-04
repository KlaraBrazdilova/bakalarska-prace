import numpy as np
from max_sub_array import max_sub_array
import matplotlib.pyplot as plt
import matplotlib

def alternating(M: np.matrix):
    # M = M[:, np.random.permutation(M.shape[1])]
    # M = M[np.random.permutation(M.shape[0]), :]
    #znovu vygenerovat alternating - ta parmutace nahodna tam nema co delat
    A = M
    no_of_iterations = 20

    for i in range(no_of_iterations):
        # utřídím řádky, transponuji matici a opakuji
        m, n = A.shape

        W = A.copy()
        W[W == 1] = 1
        W[W == 0] = -1
        tosort = np.zeros((m, 2))

        for i in range(m):
            x = max_sub_array(W[i])
            tosort[i,0] = x[0]
            tosort[i,1] = x[1]       

        perm = np.lexsort((tosort[:, 1], tosort[:, 0]))
        A = A[perm, :]
        A = A.transpose()
    return A    

folders = ["paleo", "zoo", "healthcare", "mushroom"]
for folder in folders:
    M = np.loadtxt("data/"+folder+"/"+folder+".csv",
                                    delimiter=",", dtype=int)
    vysledek = alternating(M)
    # np.savetxt("data/"+folder+"/alternating.csv", vysledek, delimiter=",", fmt='%d')
    newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
    fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
    axs.imshow(vysledek, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
    axs.set_title(folder)
    plt.savefig("data/"+folder+"/alternating/alternating.png")