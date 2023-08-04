import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matrix_product_2 import matrix_product_2

def simple_matching_coefficient(d, b):
    return np.sum(np.logical_and(d, b)) + np.sum(np.logical_and(np.logical_not(d), np.logical_not(b))) / b.size

def coverage_quality_smc(A, B, I_A,I_B):
    coverage = []
    for i in range(1, 10):
        coverage.append(simple_matching_coefficient(matrix_product_2(A[:,0:i], B[0:i,:]), matrix_product_2(I_A[:,0:i], I_B[0:i,:])))
        #coverage.append(simple_matching_coefficient(matrix_product_2(A[:,i-1:i], [B[i,:]]), matrix_product_2(I_A[:,i-1:i], [I_B[i,:]])))
        #nebo coverage.append(simple_matching_coefficient(matrix_product_2(A[:,i-1:i], [B[i,:]]), matrix_product_2(A[:,i:i+1], [B[i+1,:]])))
        #nebo coverage.append(simple_matching_coefficient(matrix_product_2(A[:,0:i], B[0:i,:]), matrix_product_2(A[:,0:i+1], B[0:i+1,:])))
    print(coverage)
    return coverage


folder = "zoo"
type = "spectral-ordering-pearson-bfp"
filter_name = "square-filter"
amount = "0.2"

I_A = np.loadtxt("data/"+folder+"/"+type+"/"+type+"-grecond-A.csv", delimiter=",", dtype=int)
I_B = np.loadtxt("data/"+folder+"/"+type+"/"+type+"-grecond-B.csv", delimiter=",", dtype=int)
A = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-A.csv", delimiter=",", dtype=int)
B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-"+amount+"-grecond-B.csv", delimiter=",", dtype=int)
# coverage_quality_smc(A, B, I)          
plt.plot(range(1,10), coverage_quality_smc(A, B, I_A, I_B), label=type+" - "+filter_name+" - "+amount+" - GreConD")

plt.tight_layout()
plt.margins(0,0)
plt.xlabel('Počet faktorů', fontsize="15")
plt.ylabel('Pokrytí', fontsize="15")
plt.title('Coverage of '+type)
plt.legend(fontsize="15")
plt.show()
# plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/GreConD/"+type+"-"+filter_name+"-grecond-coverage.png", bbox_inches='tight')        
matplotlib.pyplot.close()
print("graph done")