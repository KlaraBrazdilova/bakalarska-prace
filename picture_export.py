import numpy as np
from matplotlib import pyplot as plt
import matplotlib

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

for type in types:
    vstup = np.loadtxt("data/healthcare/"+type+"/"+type+".csv",
                    delimiter=",", dtype=int)
    

    fig, axs = plt.subplots(1, 1, figsize=(12, 9), dpi=100)
    axs.imshow(vstup, cmap=newcmp_black_white)
    axs.set_title("healthcare - "+type)

    # plt.show()
    plt.savefig("data/healthcare/"+type+"/"+type+".png")



# for type in types:
#     vstup = np.loadtxt("data/mushroom/"+type+"/"+type+".csv",
#                     delimiter=",", dtype=int)

#     newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
#     newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

#     fig, axs = plt.subplots(1, 1, figsize=(12, 9), dpi=100)
#     axs.imshow(vstup, cmap=newcmp_black_white, aspect='auto', interpolation='nearest')
#     axs.set_title("mushroom - "+type)

#     # plt.show()
#     plt.savefig("data/mushroom/"+type+"/"+type+".png")