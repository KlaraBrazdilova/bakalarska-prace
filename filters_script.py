import numpy as np
import os

from diletation import diletation
from erosion import erosion
from square_fillter import square_filter
from deleting_ones_banded_mask import banded_ones
from asso.asso import asso2
from grecond_chatgpt import GreConD

def diletation_erosion(matrix, mask):
    return diletation(erosion(matrix, mask), mask)

def erosion_diletation(matrix, mask):
    return erosion(diletation(matrix, mask), mask)

def diletation_erosion_erosion_diletation(matrix, mask):
    return diletation(erosion(erosion(diletation(matrix, mask), mask), mask), mask)

def erosion_diletation_diletation_erosion(matrix, mask):
    return erosion(diletation(diletation(erosion(matrix, mask), mask), mask), mask)

matrixes = [("col-matrix-3x2", np.array([[0, 1, 0], [0, 1, 0]])), 
            ("unit-matrix-3x3", np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])), 
            ("col-matrix-3x3", np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))]
files = ["paleo", "zoo", "mushroom", "healthcare"]
types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
filters = [{"name":"deleted-band", "function": banded_ones, "amouts": [("30", 30), ("50", 50), ("70", 70), ("90", 90)]}, 
           {"name":"square-filter", "function": square_filter, "amouts": [("0.2", 0.2), ("0.3", 0.3), ("0.4", 0.4), ("0.5", 0.5), ("0.35", 0.35)]}, 
           {"name":"diletation-erosion", "function": diletation_erosion, "amouts": matrixes}, 
           {"name":"erosion-diletation", "function": erosion_diletation, "amouts": matrixes}, 
           {"name":"diletation-erosion-erosion-diletation", "function": diletation_erosion_erosion_diletation, "amouts": matrixes}, 
           {"name":"erosion-diletation-diletation-erosion", "function": erosion_diletation_diletation_erosion, "amouts": matrixes}]
factors = [5, 10, 15]


for file in files:
    for type in types:
        M = np.loadtxt("data/"+file+"/"+type+".csv", delimiter=",", dtype=int)
        # M = np.loadtxt("data/"+file+"/"+type+"/"+type+".csv",
        #                                 delimiter=",", dtype=int)
        for filter in filters:
            filter_name = filter["name"]
            filter_amount = filter["amouts"]
            filter_function = filter["function"]
            for amount in filter_amount:
                name, val = amount
                filtred = filter_function(M, val)

                cesta1 = "data/"+file+"/"+type+"/"+filter_name+"/"
                cesta2 = "data/"+file+"/"+type+"/"+filter_name+"/GreConD/"
                cesta3 = "data/"+file+"/"+type+"/"+filter_name+"/ASSO/"
                adresar1 = os.path.dirname(cesta1)
                adresar2 = os.path.dirname(cesta2)
                adresar3 = os.path.dirname(cesta3)

                if not os.path.exists(adresar1):
                    os.makedirs(adresar1)
                if not os.path.exists(adresar2):
                    os.makedirs(adresar2)
                if not os.path.exists(adresar3):
                    os.makedirs(adresar3)    

                np.savetxt(cesta1+type+"-"+filter_name+"-"+name+".csv", filtred, delimiter=",")
                
                A, B, k = GreConD(filtred)
                np.savetxt(cesta2+type+"-"+filter_name+"-"+name+"-grecond-A.csv", A, delimiter=",")
                np.savetxt(cesta2+type+"-"+filter_name+"-"+name+"-grecond-B.csv", B, delimiter=",")
                np.savetxt(cesta2+type+"-"+filter_name+"-"+name+"-grecond-k.txt", np.array([k]), fmt="%d")

                for factor in factors:                    
                    C, D = asso2(filtred, factor, 0.9, 1, 1)
                    np.savetxt(cesta3+type+"-"+filter_name+"-"+name+"-asso-"+str(factor)+"-A.csv", C, delimiter=",") 
                    np.savetxt(cesta3+type+"-"+filter_name+"-"+name+"-asss-"+str(factor)+"-B.csv", D, delimiter=",") 
                