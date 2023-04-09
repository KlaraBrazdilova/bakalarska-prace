import numpy as np
from matrix_product import matrix_product

def GreConD(I, no_of_factors=None):
    # GRECOND implements GreConD algorithm for Boolean matrix factorization
    # usage: [A, B] = GreConD(I);
    # returns A * B = I (if the no. of factors is not limited)
    # if you are using this implementation please cite the following work
    # Belohlavek R., Vychodil V.:
    # Discovery of optimal factors in binary data via a novel method of matrix decomposition.
    # Journal of Computer and System Sciences 76(1)(2010), 3-20.

    M = np.array(I, dtype=bool)
    m, n = M.shape
    U = M
    k = 0

    A = np.zeros((m, 0), dtype=bool)
    B = np.zeros((0, n), dtype=bool)

    while np.any(U):
        v = 0
        d = np.zeros(n, dtype=bool)
        d_old = np.zeros(n, dtype=bool)
        d_mid = np.zeros(n, dtype=bool)
        e = np.ones((m, 1), dtype=bool)  # extent for speed closure

        atr = np.where(np.sum(U, axis=0) > 0)[0]  # only not covered attributes

        while True:
            for j in atr:
                if not d[j]:
                    # computes the value of the cover function for the candidate factor
                    # inline function for speed
                    # arrow down (speed version)
                    a = e & M[:, j:j+1]
                    # arrow ups
                    sum_a = np.sum(a)
                    if sum_a * n > v:  # check the size of upper bound
                        b = np.all(M[a[:, 0], :], axis=0)
                        if sum_a * np.sum(b) > v:  # check the size of upper bound
                            cost = np.sum(U[a[:, 0], :][:, b])
                            if cost > v:
                                v = cost
                                d_mid = b
                                c = a[:, 0]
            d = d_mid
            e = c

            if np.all(d == d_old):
                break
            else:
                d_old = d

        A = np.hstack((A, c[:, np.newaxis]))
        B = np.vstack((B, d[np.newaxis, :]))

        k += 1
        print(k)

        # end if the no. of factors is reached
        if no_of_factors is not None and k == no_of_factors:
            break

        # delete already covered part
        U[c, d] = False

    return A, B, k


# matrix_test = np.matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
#                       1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])
# A, B = GreConD(matrix_test)
# print(A)
# print(B)
# print(matrix_product(A, B))

M = np.loadtxt("data/paleo/paleo.csv",
                 delimiter=",", dtype=int)
A, B, k = GreConD(M)
print(k)