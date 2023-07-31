import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from coverage_guality import coverage_guality
from matrix_similarity import matrix_similarity

types = ["barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating", "spectral-ordering-pearson-bfp-fix"]
filters = [("square-filter",["0.2", "0.3", "0.4", "0.5", "0.35"] ), 
           ("diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("diletation-erosion-erosion-diletation",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("erosion-diletation-diletation-erosion",["col-matrix-3x3", "col-matrix-3x2", "unit-matrix-3x3"]), 
           ("deleted-band", ["30", "50", "70", "90"])]
folders = ["healthcare"] #"mushroom" export zvlast kvuli roztazeni , "paleo", "zoo", "healthcare"
factors = ["5", "10", "15"]

for factor in factors:
    for folder in folders:
        for type in types:
            for filter in filters:
                filter_name, filter_amount = filter
                fig, axs = plt.subplots(1, 1, figsize=(10,5))
                coverage = []
                for amount in filter_amount:
                    I = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/"+type+"-"+filter_name+"-"+amount+".csv", delimiter=",", dtype=int)
                    A = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/ASSO/"+type+"-"+filter_name+"-"+amount+"-asso-"+factor+"-A.csv", delimiter=",", dtype=int)
                    B = np.loadtxt("data/"+folder+"/"+type+"/"+filter_name+"/ASSO/"+type+"-"+filter_name+"-"+amount+"-asso-"+factor+"-B.csv", delimiter=",", dtype=int)
                    # coverage.append(coverage_guality(A, B, I))
                    print(amount)
                    plt.plot(range(1,int(factor)+2), coverage_guality(A, B, I)[1:int(factor)+2], label=type+" - "+filter_name+" - "+amount+" - ASSO - "+factor)


                plt.tight_layout()
                plt.margins(0,0)
                plt.xlabel('Počet faktorů', fontsize="15")
                plt.ylabel('Pokrytí', fontsize="15")
                plt.title('Coverage of' + type)
                plt.legend(fontsize="15")
                plt.savefig("data/"+folder+"/"+type+"/"+filter_name+"/ASSO/"+type+"-"+filter_name+"-asso"+factor+"-coverage.png", bbox_inches='tight')        
                #plt.show()
                matplotlib.pyplot.close()
                print("graph done")

# A = np.loadtxt("data/zoo/alternating/square-filter/GreConD/alternating-square-filter-0.2-grecond-A.csv",
#                  delimiter=",", dtype=int)
# B = np.loadtxt("data/zoo/alternating/square-filter/GreConD/alternating-square-filter-0.2-grecond-B.csv",
#                  delimiter=",", dtype=int)
# I = np.loadtxt("data/zoo/alternating/square-filter/alternating-square-filter-0.2.csv", delimiter=",", dtype=int)
# coverage = []


# def coverage_guality_2(product, I):
    # coverage = [] #pridat 0 na začátek
    # for i in range(1, I.shape[0]):
    #     coverage.append(matrix_similarity(product, I))
    # return coverage

# fig, axs = plt.subplots(1, 1, figsize=(10,5))
# for quantity in ["0.2", "0.3", "0.4", "0.5", "0.35"]: #, "0.4", "0.5", "0.35"
#     # A = np.loadtxt("data/paleo/alternating/square-filter/GreConD/alternating-square-filter-"+quantity+"-grecond-A.csv",
#     #              delimiter=",", dtype=int)
#     # B = np.loadtxt("data/paleo/alternating/square-filter/GreConD/alternating-square-filter-"+quantity+"-grecond-B.csv",
#     #              delimiter=",", dtype=int)
#     I = np.loadtxt("data/paleo/alternating/square-filter/alternating-square-filter-"+quantity+".csv", delimiter=",", dtype=int)
#     product = np.loadtxt("data/paleo/alternating/square-filter/alternating-square-filter-"+quantity+"-grecond-product.csv", delimiter=",", dtype=int)
#     plt.plot(range(1,I.shape[0]-1), coverage_guality_2(product, I)[1:], label="Alternating method - square filter - "+quantity+" - GreConD")
#     print(quantity)
#     # i = i+1
#     # coverage.append(coverage_guality(A, B, I)) #rovnou udělat plt.plot

# # print(coverage)

# # fig, axs = plt.subplots(1, 1, figsize=(5, 10))
# # i=0
# # for quantity in ["0.2", "0.3", "0.4", "0.5", "0.35"]:
# #     plt.plot(range(1,I.shape[0]-1), coverage[i][1:], label="Alternating method - square filter - "+quantity+" - GreConD")
# #     i = i+1

# plt.tight_layout()
# plt.margins(0,0)
# plt.xlabel('Počet faktorů', fontsize="15")
# plt.ylabel('Pokrytí', fontsize="15")
# plt.title('Pokrytí Alternating metoda - square filter - GreConD', fontsize="15")
# plt.legend(fontsize="15")
# plt.savefig("data/zoo/alternating/square-filter/GreConD/alternating-square-filter-grecond-coverage.png", bbox_inches='tight')
# plt.show()