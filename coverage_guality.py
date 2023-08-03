import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from matrix_similarity import matrix_similarity
from matrix_product import matrix_product
from matrix_product_2 import matrix_product_2

def errors(product, I):
    error = 0
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if (I[i,j] == 1 and product[i,j] == 0) or (I[i,j] == 0 and product[i,j] == 1):
                error += 1
    return error                  

def coverage_guality_2(A, B, I):
    coverage = [] #pridat 0 na začátek
    for i in range(1, I.shape[0]):
        coverage.append(1 - errors(matrix_product_2(A[:,0:i], B[0:i,:]), I) / np.sum(I))
    return coverage

def coverage_guality(A, B, I):
    coverage = [] #pridat 0 na začátek
    for i in range(1, I.shape[0]):
        coverage.append(matrix_similarity(matrix_product_2(A[:,0:i], B[0:i,:]), I))
    return coverage

# folder = "zoo"
# type = "spectral-ordering-pearson-bfp"
# filter_name = "square-filter"
# amount = "0.3"

# I = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)
# A = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-A.csv", delimiter=",", dtype=int)
# B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-B.csv", delimiter=",", dtype=int)
                

# plt.plot(range(1,I.shape[0]-1), coverage_guality(A, B, I)[1:], label=" - GreConD")

# plt.tight_layout()
# plt.margins(0,0)
# plt.xlabel('Počet faktorů', fontsize="15")
# plt.ylabel('Pokrytí', fontsize="15")
# plt.title('Coverage of Alternating method')
# plt.legend(fontsize="15")
# plt.show()
# # plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-grecond-coverage.png", bbox_inches='tight')        
# matplotlib.pyplot.close()
#nutná optimalizace - matrix_product se vysledek vzdycky stejný jak ten předešlý v cyklu, jen dojde k přidání další hodnoty?


# def coverage_guality_2(product, I):
#     coverage = [] #pridat 0 na začátek
#     for i in range(1, I.shape[0]):
#         coverage.append(matrix_similarity(product, I))
#     return coverage

# A = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-A.csv",
#                              delimiter=",", dtype=int)
# B = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-B.csv",
#                              delimiter=",", dtype=int)
# I = np.loadtxt("data/healthcare/alternating/square-filter/alternating-square-filter-0.3.csv", delimiter=",", dtype=int)
# product = np.loadtxt("data/healthcare/alternating/square-filter/GreConD/alternating-square-filter-0.3-grecond-product.csv", 
#                      delimiter=",", dtype=int)
# print("nacteno")
# print(coverage_guality_2(product,I))
# print(coverage_guality(A,B,I))