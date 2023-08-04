import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matrix_product_2 import matrix_product_2

def simple_matching_coefficient(d, b):
    return np.sum(np.logical_and(d, b)) + np.sum(np.logical_and(np.logical_not(d), np.logical_not(b))) / b.size

def coverage_quality_smc(F1,F2):
    coverage = []
    s1 = np.array([F1[:,0]])
    s2 = np.array([F2[:,0]])
    for i in range(1, 10):
        coverage_vector_s1 = []     
        for vec in s1:
            coverage_vector = []
            for vec2 in s2:                
                coverage_vector.append(simple_matching_coefficient(vec,vec2))
            # print(coverage_vector)    
            coverage_vector_s1 = np.max(coverage_vector)   
        # print(coverage_vector_s1)     
        coverage.append(np.sum(coverage_vector_s1) / s1.size)  
        s1 = np.append(s1, [F1[:,i]], axis=0)
        s2 = np.append(s2, [F2[:,i]], axis=0)
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
plt.plot(range(1,10), coverage_quality_smc(matrix_product_2(A, B), matrix_product_2(I_A,I_B)), label=type+" - "+filter_name+" - "+amount+" - GreConD")

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