import numpy as np
from asso import asso2

slozky = ["paleo", "zoo", "mushroom", "healthcare"]
typy = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating"]

for slozka in slozky:
    M = np.loadtxt("data/"+slozka+"/"+slozka+".csv",
                        delimiter=",", dtype=int)
    A, B = asso2(M, 5, 0.9, 1, 1)
    np.savetxt("data/"+slozka+"/"+slozka+"-asso-5-A.csv", A, delimiter=",") 
    np.savetxt("data/"+slozka+"/"+slozka+"-asso-5-B.csv", B, delimiter=",") 
    
    # for typ in typy:
    #     M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
    #                     delimiter=",", dtype=int)
    #     A, B = asso2(M, 5, 0.9, 1, 1)
    #     np.savetxt("data/"+slozka+"/"+typ+"-asso-5-A.csv", A, delimiter=",") 
    #     np.savetxt("data/"+slozka+"/"+typ+"-asso-5-B.csv", B, delimiter=",") 
            