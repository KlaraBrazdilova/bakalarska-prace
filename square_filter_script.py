import copy
import numpy as np
from grecond_chatgpt import GreConD

from square_fillter import square_filter

slozky = ["paleo","zoo", "mushroom", "healthcare"]
typy = ["spectral-ordering-pearson-bfp","barycenter-bfp","alternating"]
amount = [0.2, 0.3, 0.35, 0.4, 0.5]
for i in amount:
    for slozka in slozky:
        for typ in typy:
            M = np.loadtxt("data/"+slozka+"/square-filter/"+typ+"/"+typ+"-square-filter-"+ str(i) +".csv",
                            delimiter=",", dtype=int)
            A, B, k = GreConD(M)
            np.savetxt("data/"+slozka+"/square-filter/"+typ+"/"+typ+"-square-filter-"+ str(i) +"-grecond-A.csv", A, delimiter=",") 
            np.savetxt("data/"+slozka+"/square-filter/"+typ+"/"+typ+"-square-filter-"+ str(i) +"-grecond-B.csv", B, delimiter=",") 
            np.savetxt("data/"+slozka+"/square-filter/"+typ+"/"+typ+"-square-filter-"+ str(i) +"-grecond-k.txt", np.array([k]), fmt="%d") 
            # M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
            #                 delimiter=",", dtype=int)
            # vstup = copy.deepcopy(M)
            # deleted = square_filter(3, M, i)  
            # print(deleted)

            # np.savetxt("data/"+slozka+"/square-filter/"+typ+"/"+typ+"-square-filter-"+ str(i) +".csv", deleted, delimiter=",") 