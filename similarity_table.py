import numpy as np

from matrix_similarity import simple_matching_coefficient


types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("deleted-band", ["30", "50", "70", "90"]), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"])]
folders = ["paleo", "zoo", "healthcare", "mushroom"] 

output = []
for folder in folders:
    for type in types:
        permuted = np.loadtxt("data/"+folder+"/"+type+"/"+type+".csv", delimiter=",", dtype=int)
        line = [folder+"-"+type]
        for filter in filters:
            filter_name, filter_amount = filter
            line.append(filter_name)
            for amount in filter_amount:
                filtered = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)
                a = str(np.around(simple_matching_coefficient(filtered, permuted), 2))
                line.append(a)

        output.append(line)

np.savetxt("data/simple_matching_coefficient-procenta.csv", output, delimiter=",", fmt='%s')