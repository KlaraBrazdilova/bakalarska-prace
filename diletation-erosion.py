import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import copy

from grecond_chatgpt import GreConD
from diletation import diletation
from erosion import erosion
from asso.asso import asso2


slozky = ["paleo","zoo", "healthcare", "mushroom"]
typy = ["spectral-ordering-pearson-bfp","barycenter-bfp","alternating"]
maks = [("col-matrix-3x2", np.array([[0, 1, 0], [0, 1, 0]])), ("col-matrix-3x3", np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])), ("unit-matrix-3x3", np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))] 

# amount = [0.2, 0.3, 0.35, 0.4, 0.5]

for mask_type in maks:
    mask_name, mask = mask_type
    for slozka in slozky:
        for typ in typy:
            M = np.loadtxt("data/"+slozka+"/"+typ+"/diletation-erosion/"+typ+"-"+mask_name+".csv",
                            delimiter=",", dtype=int)
            vstup = copy.deepcopy(M)
            dilet = diletation(M, mask)
            final = erosion(dilet, mask)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+".csv", final, delimiter=",")
            
            A, B, k = GreConD(final)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"diletation-erosion-erosion-diletation-"+mask_name+"-grecond-A.csv", A, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"diletation-erosion-erosion-diletation-"+mask_name+"-grecond-B.csv", B, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"diletation-erosion-erosion-diletation-"+mask_name+"-grecond-k.txt", np.array([k]), fmt="%d")
            
            C, D = asso2(final, 5, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-5-A.csv", C, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-5-B.csv", D, delimiter=",")
            
            E, F = asso2(final, 10, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-10-A.csv", E, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-10-B.csv", F, delimiter=",")
            
            G, H = asso2(final, 15, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-15-A.csv", G, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-15-B.csv", H, delimiter=",")
            
            print(slozka, typ)

# M = np.loadtxt("data/zoo/alternating.csv",
#                         delimiter=",", dtype=int)
# mask = np.array([[0, 1, 0], [0, 1, 0]])
# vstup = copy.deepcopy(M)
# dilet = diletation(M, mask)
# eros = erosion(dilet, mask)

# newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue', 'green'])
# newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
# fig, axs = plt.subplots(1, 3, figsize=(10, 5))
# axs[0].imshow(vstup, cmap=newcmp_black_white)
# axs[0].set_title('Original')
# axs[1].imshow(dilet, cmap=newcmp_black_white)
# axs[1].set_title('diletation')
# axs[2].imshow(eros, cmap=newcmp_black_white)
# axs[2].set_title('erosion after diletation')
# plt.show()