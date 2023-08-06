import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from coverage_guality import coverage_guality_2


types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("deleted-band", ["30", "50", "70", "90"])]
folders = ["mushroom", "paleo", "zoo", "healthcare"]

for folder in folders:
    for type in types:
        for filter in filters:
            filter_name, filter_amount = filter
            fig, axs = plt.subplots(1, 1, figsize=(10,5))
            coverage = []
            for amount in filter_amount:
                I = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)
                A = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-A.csv", delimiter=",", dtype=int)
                B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-B.csv", delimiter=",", dtype=int)
                # coverage.append(coverage_guality(A, B, I))
                print(amount)
                plt.plot(range(1,I.shape[0]-1), coverage_guality_2(A, B, I)[1:], label=type+" - "+filter_name+" - "+amount+" - GreConD")

            plt.tight_layout()
            plt.margins(0,0)
            plt.xlabel('Počet faktorů', fontsize="15")
            plt.ylabel('Pokrytí', fontsize="15")
            plt.title('Coverage of '+type)
            plt.legend(fontsize="15")
            # plt.show()
            plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-grecond-coverage.png", bbox_inches='tight')        
            matplotlib.pyplot.close()