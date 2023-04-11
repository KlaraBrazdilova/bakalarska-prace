import numpy as np
from scipy.sparse import csr_matrix
from matrix_product import matrix_product
from matrix_similarity import matrix_similarity

def GreConD(I, no_of_factors=None):
    # GRECOND implements GreConD algorithm for Boolean matrix factorization
    # usage: [A, B] = GreConD(I);
    # returns A \circ B = I (if the no. of factors is not limited)
    # if you are using this implementation please cite the following work
    # Belohlavek R., Vychodil V.:
    # Discovery of optimal factors in binary data via a novel method of matrix decomposition.
    # Journal of Computer and System Sciences 76(1)(2010), 3-20.

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
        #e = csr_matrix(np.ones((m, 1), dtype=bool))  # extent for speed closure
        e = np.ones((m, 1), dtype=bool)
        #atr = U.sum(axis=0).nonzero()[1]  # only not covered attributes
        atr = np.where(np.sum(U, axis=0) > 0)[0]
        while True:
            for j in atr:
                if not d[j]:
                    # computes the value of the cover function for the candidate factor
                    # inline function for speed
                    # arrow down (speed version)
                    #a = e.multiply(M[:,j].reshape(-1,1))
                    a = e & M[:, j:j+1]
                    # arrow ups
                    sum_a = a.sum()
                    #sum_a = np.sum(a)
                    if sum_a*n > v:  # check the size of upper bound
                        #b = M[a,:].all(axis=0)
                        #print(a)
                        b = np.all(M[a[:, 0], :], axis=0)
                        if sum_a*b.sum() > v:  # check the size of upper bound
                            cost = U[a[:,0],:][:,b].sum()
                            # cost = np.sum(U[a[:, 0], :][:, b])
                            if cost > v:
                                v = cost
                                d_mid = b
                                c = a
                                #c = a[:, 0]

            d = d_mid
            e = c

            if np.all(d==d_old):
                break
            else:
                d_old = d

        print('su tu')
        #A = np.hstack((A, c.toarray()))
        # print(c[:, np.newaxis])
        #A = np.hstack((A, c[:, np.newaxis]))
        A = np.concatenate((A, c), axis=1)
        B = np.vstack((B, d[np.newaxis, :]))

        k += 1
        print(k)

        # end if the no. of factors is reached
        if no_of_factors is not None and k==no_of_factors:
            break

        # delete already covered part
        for i in range(m):
            for j in range(n):
                if c[i, 0] and d[j]:
                    U[i, j] = False
  
        #U[c, d] = False

    return A.astype(bool), B.astype(bool), k




# matrix_test = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
#                       1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])
# A, B = GreConD(matrix_test)
# print(A)
# print(B)
# print(matrix_product(A, B))

M = np.loadtxt("data/zoo/zoo.csv",
                 delimiter=",", dtype=int)
A, B, k = GreConD(M)

print(k)
prod = matrix_product(A, B)
print(matrix_similarity(M, prod))