import numpy as np
from asso import asso2

files = ["paleo"] #"mushroom", "paleo"
types = ["barycenter-bfp"]#"spectral-ordering-pearson-bfp-fix", "alternating", "barycenter", "barycenter-bfp-alternating"
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] )]# ("deleted-band", ["30", "50", "70", "90"]), ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"])]
factors = [5, 10, 15]


for file in files:
    for type in types:
        for filter in filters:
            filter_name, filter_amount = filter
            for amount in filter_amount:
                for factor in factors:
                    M = np.loadtxt("data/"+file+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+str(amount)+".csv",
                                        delimiter=",", dtype=int)
                    A, B = asso2(M, factor, 0.9, 1, 1)
                    np.savetxt("data/"+file+"/"+type+"/"+filter_name+"/ASSO/"+type+"-"+filter_name+"-"+str(amount)+"-asso-"+str(factor)+"-A.csv", A, delimiter=",") 
                    np.savetxt("data/"+file+"/"+type+"/"+filter_name+"/ASSO/"+type+"-"+filter_name+"-"+str(amount)+"-asso-"+str(factor)+"-B.csv", B, delimiter=",") 
                