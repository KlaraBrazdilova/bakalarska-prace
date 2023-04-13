import numpy as np
from matplotlib import pyplot as plt
import matplotlib

vstup = np.loadtxt("data/zoo/alternating.csv",
                 delimiter=",", dtype=int)
deleted = np.loadtxt("data/zoo/alternating-deleted-band-90-changes.csv",
                 delimiter=",", dtype=int)

newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')

axs[1].imshow(deleted, cmap=newcmp)
axs[1].set_title('Deleting 90 %')

plt.show()