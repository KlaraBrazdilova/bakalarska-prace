import numpy as np

from matrix_similarity import similarity_2

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("deleted-band", ["30", "50", "70", "90"]), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"])]
folders = ["paleo", "zoo", "healthcare", "mushroom"] 

# permuted = np.loadtxt("data/zoo/alternating.csv", delimiter=",", dtype=int)
# filtered = np.loadtxt("data/zoo/alternating/square-filter/alternating-square-filter-0.2.csv", delimiter=",", dtype=int)
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
                a = str(np.around(similarity_2(filtered, permuted), 2))
                # print(a)
                line.append(a)
                # print(folder + "-" + type + "-" + filter_name + "-" + amount + ": " + str(matrix_similarity(permuted, filtered)))
        # print(line)
        output.append(line)

np.savetxt("data/similarity_2.csv", output, delimiter=",", fmt='%s')