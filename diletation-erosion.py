import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import copy

from grecond_chatgpt import GreConD
from diletation import diletation
from erosion import erosion

# M = np.loadtxt('data/healthcare/alternating.csv', delimiter=',', dtype=int)
# vstup = copy.deepcopy(M)
# mask = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# dilet = diletation(M, mask)
# eros = erosion(dilet, mask)


# slozky = ["paleo","zoo", "mushroom", "healthcare"]
# typy = ["spectral-ordering-pearson-bfp","barycenter-bfp","alternating"]
# mask = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
# # amount = [0.2, 0.3, 0.35, 0.4, 0.5]
# for slozka in slozky:
#     for typ in typy:            
#         # M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
#         #                 delimiter=",", dtype=int)
#         # vstup = copy.deepcopy(M)
#         # dilet = diletation(M, mask)
#         # eros = erosion(dilet, mask)
#         # print(slozka, typ)
#         # np.savetxt("data/"+slozka+"/diletation-erosion/"+typ+"/"+typ+"-col-matrix-3x3.csv", eros, delimiter=",") 
#         M = np.loadtxt("data/"+slozka+"/diletation-erosion/"+typ+"/"+typ+"-col-matrix-3x3.csv",
#                         delimiter=",", dtype=int)
#         A, B, k = GreConD(M)

#         print(slozka, typ)
#         np.savetxt("data/"+slozka+"/diletation-erosion/"+typ+"/"+typ+"-col-matrix-3x3-grecond-A.csv", A, delimiter=",") 
#         np.savetxt("data/"+slozka+"/diletation-erosion/"+typ+"/"+typ+"-col-matrix-3x3-grecond-B.csv", B, delimiter=",") 
#         np.savetxt("data/"+slozka+"/diletation-erosion/"+typ+"/"+typ+"-col-matrix-3x3-grecond-k.txt", np.array([k]), fmt="%d") 

M = np.loadtxt("data/zoo/alternating.csv",
                        delimiter=",", dtype=int)
mask = np.array([[0, 1, 0], [0, 1, 0]])
vstup = copy.deepcopy(M)
dilet = diletation(M, mask)
eros = erosion(dilet, mask)

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue', 'green'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')
axs[1].imshow(dilet, cmap=newcmp_black_white)
axs[1].set_title('diletation')
axs[2].imshow(eros, cmap=newcmp_black_white)
axs[2].set_title('erosion after diletation')
plt.show() 