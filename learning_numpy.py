import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.1)  # Generate x values
y1 = np.sin(x)  # Generate y values using algorithm 1
# y2 = np.cos(x)  # Generate y values using algorithm 2
print(x)
y1 = [1500, 1520, 1530, 1590, 1570, 1550, 1530, 1510, 1580, 1600]
plt.plot(x, y1, label='Algorithm 1')
# plt.plot(x, y2, label='Algorithm 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Algorithms')
plt.legend()

plt.show()