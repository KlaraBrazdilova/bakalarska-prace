import numpy as np
from asso import asso2

slozky = ["paleo", "zoo", "mushroom", "healthcare"]
typy = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating"]

for slozka in slozky:
    M = np.loadtxt("data/"+slozka+"/"+slozka+".csv",
                        delimiter=",", dtype=int)
    A, B = asso2(M, 10, 0.9, 1, 1)
    np.savetxt("data/"+slozka+"/"+slozka+"-asso-A.csv", A, delimiter=",") 
    np.savetxt("data/"+slozka+"/"+slozka+"-asso-B.csv", B, delimiter=",") 
    
    for typ in typy:
        M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
                        delimiter=",", dtype=int)
        A, B = asso2(M, 10, 0.9, 1, 1)
        np.savetxt("data/"+slozka+"/"+typ+"-asso-A.csv", A, delimiter=",") 
        np.savetxt("data/"+slozka+"/"+typ+"-asso-B.csv", B, delimiter=",") 
            