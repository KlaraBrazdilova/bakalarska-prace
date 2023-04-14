from matplotlib import pyplot as plt
import matplotlib
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

for i in [30, 50, 70, 90]:
    slozka = "paleo"
    typ = "alternating"#"spectra-ordering-pearson-bfp"#"barycenter-bfp"#"alternating"
    cislo = i
    M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
                    delimiter=",", dtype=int)
    vstup = copy.deepcopy(M)
    band, deleted = banded_ones(M, cislo)  
    print(deleted)

    # newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
    # newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

    # fig, axs = plt.subplots(1, 3, figsize=(10, 5))
    # axs[0].imshow(vstup, cmap=newcmp_black_white)
    # axs[0].set_title('Original')

    # axs[1].imshow(band, cmap=newcmp_black_white)
    # axs[1].set_title('Band')

    # axs[2].imshow(deleted, cmap=newcmp)
    # axs[2].set_title('Deleting')


    # plt.show()
    np.savetxt("data/"+slozka+"/"+typ+"-deleted-band-"+ str(cislo) +"-changes.csv", deleted, delimiter=",") 

    for i in range(deleted.shape[0]):
        for j in range(deleted.shape[1]):
            if deleted[i,j] == 2:
                deleted[i,j] = 0

    np.savetxt("data/"+slozka+"/"+typ+"-deleted-band-"+ str(cislo) +".csv", deleted, delimiter=",")         