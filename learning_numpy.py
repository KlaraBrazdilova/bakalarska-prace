import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# x = np.arange(0, 1, 0.1)  # Generate x values
# y1 = np.sin(x)  # Generate y values using algorithm 1
# # y2 = np.cos(x)  # Generate y values using algorithm 2
# print(x)
# y1 = [1500, 1520, 1530, 1590, 1570, 1550, 1530, 1510, 1580, 1600]
# plt.plot(x, y1, label='Algorithm 1')
#  plt.tight_layout()
# # plt.plot(x, y2, label='Algorithm 2')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Comparison of Algorithms')
# plt.legend()

# plt.show()

dileter = np.loadtxt("bakalarska-prace/data/zoo/zoo.csv",delimiter=",", dtype=int)

newcmp_black_white = matplotlib.colors.LinearSegmentedColormap.from_list("", ['white','black'])
fig, axs = plt.subplots(1, 1, figsize=(12, 9)) 
plt.tight_layout()
axs.imshow(dileter, cmap=newcmp_black_white) #pro mushroom aspect='auto', interpolation='nearest'
plt.savefig("bakalarska-prace/data/pokus4.png", bbox_inches='tight')       

plt.show()
matplotlib.pyplot.close()