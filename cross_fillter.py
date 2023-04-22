import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def cross_count(M, size, i, j):
    """Count number of 1s in square of size size around (i,j)."""
    count = 0
    max = size//2

    #radky
    for row in range(i-max, i+max+1):
        for col in range(0, M.shape[1]):
            try:
                if M[row, col]:
                    count += 1
            except IndexError:
                pass
    # print(count) 
    #sloupce       
    for col in range(j-max, j+max+1):
        for row in range(0, M.shape[0]):
            # for k in range(max+1):
            try:
                if M[row, col]:
                    count += 1
            except IndexError:
                pass       

    #zapocitavam dvakrat prekrizene radky a sloupce
    for row in range(i-max, i+max+1):
        for col in range(j-max, j+max+1):
            try:
                if M[row, col]:
                    count -= 1
            except IndexError:
                pass   

    # print(count)
    # print(M.shape)
    # print((size*M.shape[0] + size*M.shape[1]))
    # print(count/(size*M.shape[0] + size*M.shape[1] - size*size))
    return count/(size*M.shape[0] + size*M.shape[1]- size*size)

def cross_filter(size, M, limit):
    """Filter matrix with square filter of size size."""
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if cross_count(M, size, i, j) > limit:
                # print("Su tu")                
                if not M[i,j]:
                    M[i, j] = 1 #2
            else:
                if M[i,j]:
                    M[i, j] = 0 #3     
    return M


M = np.loadtxt('data/paleo/spectra-ordering-pearson-bfp.csv', delimiter=',', dtype=int)
vstup = M.copy()
filter = cross_filter(3, M, 0.3)
# print(M)
newcmp = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black', 'blue', 'green'])
newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(vstup, cmap=newcmp_black_white)
axs[0].set_title('Original')
axs[1].imshow(filter, cmap=newcmp_black_white)
axs[1].set_title('filter, 3, 0.7')
plt.show()