import numpy as np
from asso import asso2

files = ["paleo", "zoo", "mushroom", "healthcare"]
types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating"]
filters = ["deleted-band", "square-filter", "diletation-erosion", "erosion-diletation", "diletation-erosion-erosion-diletation", "erosion-diletation-diletation-erosion"]
factors = [5, 10, 15]
filters_level = ["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"] #diletation-erosion
["30", "50", "70", "90"] #deleted-band
["0.2", "0.3", "0.4", "0.5", "0.35"] #square-filter


for file in files:
    for type in types:
        for filter in filters:
            for factor in factors:
                M = np.loadtxt("data/"+file+"/"+type+"/"+filter+".csv",
                                    delimiter=",", dtype=int)
                A, B = asso2(M, 5, 0.9, 1, 1)
                np.savetxt("data/"+file+"/"+type+"-asso-5-A.csv", A, delimiter=",") 
                np.savetxt("data/"+file+"/"+type+"-asso-5-B.csv", B, delimiter=",") 
    
    # for typ in typy:
    #     M = np.loadtxt("data/"+slozka+"/"+typ+".csv",
    #                     delimiter=",", dtype=int)
    #     A, B = asso2(M, 5, 0.9, 1, 1)
    #     np.savetxt("data/"+slozka+"/"+typ+"-asso-5-A.csv", A, delimiter=",") 
    #     np.savetxt("data/"+slozka+"/"+typ+"-asso-5-B.csv", B, delimiter=",") 
            