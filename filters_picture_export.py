import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
types = ["spectral-ordering-pearson-bfp-fix", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), ("deleted-band", ["30", "50", "70", "90"])] #("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]),
folders = ["paleo", "zoo", "healthcare"] #"mushroom" export zvlast kvuli roztazeni , "paleo", "zoo", "healthcare"
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])


for folder in folders:
    for type in types:
        for filter in filters:
            filter_name, filter_amount = filter
            for amount in filter_amount:
                original = np.loadtxt("bakalarska-prace/data/"+folder+"/"+type+"/"+type+".csv",
                                    delimiter=",", dtype=int)
                filtered = np.loadtxt("bakalarska-prace/data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)

                fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
                plt.tight_layout()
                axs.imshow(filtered, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
                axs.set_title(folder + "-" + type + "-" + filter_name + "-" + amount)
                plt.savefig("bakalarska-prace/data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".png", bbox_inches='tight')       
                matplotlib.pyplot.close()

                changes = filtered 
                for i in range(filtered.shape[0]):
                    for j in range(filtered.shape[1]):
                        if filtered[i,j] != original[i,j]:
                            changes[i,j] = 2                

                fig, axs = plt.subplots(1, 1, figsize=(12, 9))
                plt.tight_layout() 
                axs.imshow(changes, cmap=newcmp) # pro mushroom aspect='auto', interpolation='nearest'
                axs.set_title(folder + "-" + type + "-" + filter_name + "-" + amount + "-changes")   
                plt.savefig("bakalarska-prace/data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+"-changes.png", bbox_inches='tight')
                matplotlib.pyplot.close()  

                