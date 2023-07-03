import numpy as np
from matplotlib import pyplot as plt
import matplotlib

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"])]
folders = ["paleo", "zoo", "healthcare"] #"mushroom" export zvlast kvuli roztazeni
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])


for folder in folders:
    for type in types:
        for filter in filters:
            filter_name, filter_amount = filter
            for amount in filter_amount:
                original = np.loadtxt("data/"+folder+"/"+type+"/"+type+".csv",
                                    delimiter=",", dtype=int)
                filtered = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)

                changes = filtered 
                for i in range(filtered.shape[0]):
                    for j in range(filtered.shape[1]):
                        if filtered[i,j] != original[i,j]:
                            changes[i,j] = 2

                fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
                axs.imshow(filtered, cmap=newcmp_black_white)
                axs.set_title(folder + "-" + type + "-" + filter_name + "-" + amount)
                plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".png")       
                matplotlib.pyplot.close()

                fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
                axs.imshow(changes, cmap=newcmp)
                axs.set_title(folder + "-" + type + "-" + filter_name + "-" + amount + "-changes")   
                plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+"-changes.png")
                matplotlib.pyplot.close()  

                