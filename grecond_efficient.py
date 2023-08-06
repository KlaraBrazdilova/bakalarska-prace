import numpy as np
from scipy.sparse import csr_matrix
from matrix_product import matrix_product
from matrix_similarity import matrix_similarity

def GreConD(I, no_of_factors=None):
    # implements GreConD algorithm for Boolean matrix factorization
    # Belohlavek R., Vychodil V.:
    # Discovery of optimal factors in binary data via a novel method of matrix decomposition.
    # Journal of Computer and System Sciences 76(1)(2010), 3-20.
    # more efficient version then grecond.py
    

    M = np.asarray(I, dtype=bool)
    m, n = M.shape
    U = M

    A = np.zeros((m, 0), dtype=bool)
    B = np.zeros((0, n), dtype=bool)

    k = 0

    while np.any(U):
        v = 0
        d = np.zeros(n, dtype=bool)
        d_old = np.zeros(n, dtype=bool)
        d_mid = np.zeros(n, dtype=bool)
        e = np.ones((m, 1), dtype=bool)
        atr = np.where(np.sum(U, axis=0) > 0)[0]
        while True:
            for j in atr:
                if not d[j]:
                    # computes the value of the cover function for the candidate factor
                    # inline function for speed
                    # arrow down (speed version)
                    a = e & M[:, j:j+1]
                    # arrow ups
                    sum_a = a.sum()
                    if sum_a*n > v:  # check the size of upper bound
                        b = np.all(M[a[:, 0], :], axis=0)
                        if sum_a*b.sum() > v:  # check the size of upper bound
                            cost = U[a[:,0],:][:,b].sum()
                            if cost > v:
                                v = cost
                                d_mid = b
                                c = a

            d = d_mid
            e = c

            if np.all(d==d_old):
                break
            else:
                d_old = d

        A = np.concatenate((A, c), axis=1)
        B = np.vstack((B, d[np.newaxis, :]))

        k += 1

        # end if the no. of factors is reached
        if no_of_factors is not None and k==no_of_factors:
            break

        # delete already covered part
        for i in range(m):
            for j in range(n):
                if c[i, 0] and d[j]:
                    U[i, j] = False

    return A.astype(bool), B.astype(bool), k

types = ["spectral-ordering-pearson-bfp", "barycenter-bfp", "alternating", "barycenter", "barycenter-bfp-alternating"]
folders = ["paleo","zoo", "mushroom", "healthcare"]
for folder in folders:
    for type in types:
        A,B,k = GreConD(np.loadtxt("data/"+folder+"/"+type+"/"+type+".csv", delimiter=",", dtype=int))
        np.savetxt("data/"+folder+"/"+type+"/"+type+"-grecond-A.csv", A, delimiter=",")
        np.savetxt("data/"+folder+"/"+type+"/"+type+"-grecond-B.csv", B, delimiter=",")
        np.savetxt("data/"+folder+"/"+type+"/"+type+"-grecond-k.txt", [k], delimiter=",")
