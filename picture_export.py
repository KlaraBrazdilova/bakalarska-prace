import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# types = ["spectral-ordering-pearson-bfp-fix", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
# folders = ["paleo", "zoo", "healthcare"]

# for folder in folders:
#     for type in types:

folder = "paleo"


data = np.loadtxt("data/"+folder+"/"+folder+".csv", delimiter=",", dtype=int)
fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
plt.tight_layout()
axs.imshow(data, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
plt.show()                      
# plt.savefig("data/"+folder+"/"+type+"/"+type+".png", bbox_inches='tight', dpi=300)       
matplotlib.pyplot.close()



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