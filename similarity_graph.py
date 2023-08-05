import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matrix_product_2 import matrix_product_2


def simple_matching_coefficient(d, b):
    return (np.sum(np.logical_and(d, b)) + np.sum(np.logical_and(np.logical_not(d), np.logical_not(b)))) / d.size

def coverage_quality_smc(F1,F2,factors):
    coverage = []
    s1 = np.array([F1[0, :]])
    s2 = np.array([F2[0, :]])
    for i in range(1, factors):
        coverage_vector_s1 = []     
        for vec in s1:
            coverage_vector = []
            for vec2 in s2:            
                coverage_vector.append(simple_matching_coefficient(vec,vec2))
            # print(coverage_vector)    
            coverage_vector_s1.append(np.max(coverage_vector))   
        # print(coverage_vector_s1)     
        coverage.append(np.sum(coverage_vector_s1) / s1.shape[0])
        s1 = np.append(s1, [F1[i, :]], axis=0)
        s2 = np.append(s2, [F2[i, :]], axis=0)
    # print(coverage)
    return coverage

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("deleted-band", ["30", "50", "70", "90"])]
folders = ["paleo"] #"mushroom" export zvlast kvuli roztazeni , "paleo", "zoo", "healthcare"

for folder in folders:
    for type in types:
        I_B = np.loadtxt("data/"+folder+"/"+type+"/"+type+"-grecond-B.csv", delimiter=",", dtype=int)
        for filter in filters:
            filter_name, filter_amount = filter
            fig, axs = plt.subplots(1, 1, figsize=(10,5))
            for amount in filter_amount:
                B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-B.csv", delimiter=",", dtype=int)
                factors = min(B.shape[0], I_B.shape[0])
                plt.plot(range(1,factors), coverage_quality_smc(B, I_B, factors), label=type+" - "+filter_name+" - "+amount+" - GreConD")

            plt.tight_layout()
            plt.margins(0,0)
            plt.xlabel('Počet faktorů', fontsize="15")
            plt.ylabel('Podobnost faktorů', fontsize="15") 
            plt.legend(fontsize="15")
            # plt.show()
            plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-grecond-similarity.png", bbox_inches='tight')        
            matplotlib.pyplot.close()
            print("graph done")