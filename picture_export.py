import numpy as np
from matplotlib import pyplot as plt
import matplotlib

vstup = np.loadtxt("data/mushroom/mushroom.csv",
                 delimiter=",", dtype=int)
# deleted = np.loadtxt("data/zoo/alternating-deleted-band-90-changes.csv",
#                  delimiter=",", dtype=int)

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

fig, axs = plt.subplots(1, 1, figsize=(16, 9), dpi=100)
# axs = plt.axes([0, 0.6, 1, 1])
# plt.xlim(0,100)
# plt.subplot(2,1,2)
# plt.hist(vstup,bins=300)
# plt.xlim(0,100)
axs.imshow(vstup, cmap=newcmp_black_white, aspect='auto', interpolation='bicubic')
axs.set_title('Original')

# axs[1].imshow(deleted, cmap=newcmp)
# axs[1].set_title('Deleting 90 %')

plt.show()