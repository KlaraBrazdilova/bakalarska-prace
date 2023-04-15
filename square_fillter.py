import numpy as np
from matplotlib import pyplot as plt
import matplotlib

def square_count(M, size, i, j):
    count = 0
    for k in range(size):
        for l in range(size):
            try:
                if M[i + k, j + l]:
                    count += 1
                if M[i - k, j - l]:
                    count += 1 
            except IndexError:
                pass    
    print(count/(size+1))            
    return count/(size+1)



def square_filter(size, M, limit):
    """Filter matrix with square filter of size size."""
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if square_count(M, size, i, j) < limit:
                M[i, j] = 0
            else:
                M[i, j] = 1
    return M

M = np.loadtxt('data/zoo/barycenter-bfp.csv', delimiter=',', dtype=int)
vstup = M.copy()
M = square_filter(2, M, 0.9)
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')
axs[1].imshow(M, cmap=newcmp_black_white)
axs[1].set_title('filter 2, 0.2')
plt.show()