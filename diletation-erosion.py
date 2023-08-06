import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import copy

from grecond_efficient import GreConD
from diletation import diletation
from erosion import erosion
from asso.asso import asso2


slozky = ["paleo","zoo", "healthcare", "mushroom"]
typy = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating"]
maks = [("col-matrix-3x2", np.array([[0, 1, 0], [0, 1, 0]])), 
        ("unit-matrix-3x3", np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])), 
        ("col-matrix-3x3", np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))] 
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

for mask_type in maks:
    mask_name, mask = mask_type
    for slozka in slozky:
        for typ in typy:
            M = np.loadtxt("data/"+slozka+"/"+typ+"/"+typ+".csv",
                            delimiter=",", dtype=int)
            
            vstup = copy.deepcopy(M)

            dilet = diletation(M, mask)
            final = erosion(dilet, mask) #diletation-erosion, you can change the order for erosion-diletation
            dileter= diletation(erosion(final, mask), mask) #diletation-erosion-erosion-diletation, you can change the order for erosion-diletation-diletation-erosion

            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/"+typ+"-diletation-erosion-"+mask_name+".csv", final, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+".csv", dileter, delimiter=",")
            
            A, B, k = GreConD(final)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/GreConD/"+typ+"-diletation-erosion-"+mask_name+"-grecond-A.csv", A, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/GreConD/"+typ+"-diletation-erosion-"+mask_name+"-grecond-B.csv", B, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/GreConD/"+typ+"-diletation-erosion-"+mask_name+"-grecond-k.txt", np.array([k]), fmt="%d")
            
            C, D = asso2(final, 5, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-5-A.csv", C, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-5-B.csv", D, delimiter=",")
            
            E, F = asso2(final, 10, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-10-A.csv", E, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-10-B.csv", F, delimiter=",")
            
            G, H = asso2(final, 15, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-15-A.csv", G, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion/ASSO/"+typ+"-diletation-erosion-"+mask_name+"-asso-15-B.csv", H, delimiter=",")
            
            A, B, k = GreConD(dileter)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-grecond-A.csv", A, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-grecond-B.csv", B, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/GreConD/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-grecond-k.txt", np.array([k]), fmt="%d")
            
            C, D = asso2(dileter, 5, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-5-A.csv", C, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-5-B.csv", D, delimiter=",")
            
            E, F = asso2(dileter, 10, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-10-A.csv", E, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-10-B.csv", F, delimiter=",")
            
            G, H = asso2(dileter, 15, 0.9, 1, 1)
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-15-A.csv", G, delimiter=",")
            np.savetxt("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/ASSO/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+"-asso-15-B.csv", H, delimiter=",")
            
            fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
            plt.tight_layout()
            axs.imshow(final, cmap=newcmp_black_white) 
            plt.savefig("data/"+slozka+"/"+typ+"/diletation-erosion/"+typ+"-diletation-erosionn-"+mask_name+".png", bbox_inches='tight')       
            matplotlib.pyplot.close()

            fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
            plt.tight_layout()
            axs.imshow(dileter, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
            plt.savefig("data/"+slozka+"/"+typ+"/diletation-erosion-erosion-diletation/"+typ+"-diletation-erosion-erosion-diletation-"+mask_name+".png", bbox_inches='tight')       
            matplotlib.pyplot.close()