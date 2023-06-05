# import numpy as np


# def asso(M, k, tau, w_p, w_m):
#     m,n = M.shape
#     A = np.log([])
#     B = np.log([])
#     neg_M = -M

#     association_matrix = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if np.sum(np.multiply(M[:,i], M[:,j])) / np.sum(M[:,i]) > tau:
#                 association_matrix[i,j] = 1

#     for factor in range(k):
#         cardinate_final_cover = np.zeros((1,m)) 
#         final_collumn = np.cell(1,n)

import numpy as np

def asso2(M, k, tau, w_p, w_m):
    # init
    m, n = M.shape
    A = np.array([], dtype=bool)
    B = np.array([], dtype=bool)
    negM = ~M

    # association matrix
    association_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if np.sum(np.multiply(M[:, i], M[:, j])) / np.sum(M[:, i]) > tau:
                association_matrix[i, j] = 1

    # Asso algorithm
    for factor in range(k):
        candidate_final_cover = np.zeros(m)
        final_column = [np.array([], dtype=bool)] * n
        print(factor)

        # product = np.hstack((A, np.zeros((m, 1), dtype=bool))) @ np.vstack((B, np.zeros((1, n), dtype=bool)))
        product = np.logical_and(np.hstack((A, np.zeros((m, 1), dtype=bool))), np.vstack((B, np.zeros((1, n), dtype=bool))))
        cover_base = w_p * np.sum(np.sum(M[product])) - w_m * np.sum(np.sum(negM[product]))

        # loop over all candidate (rows in association matrix)
        for j in range(association_matrix.shape[0]):
            final_column[j] = np.zeros(m, dtype=bool)
            candidate_row = association_matrix[j, :]

            # vectorized loop over all rows
            changed = np.logical_and(~product, np.tile(candidate_row, (m, 1)))  # check only changed values
            
            covered_by_change = np.logical_and(M, changed)
            overcovered_by_change = np.logical_and(negM, changed)
            cover_aktualni = cover_base + w_p * np.sum(covered_by_change, axis=1) - w_m * np.sum(overcovered_by_change, axis=1)

            final_column[j][cover_base < cover_aktualni] = 1

            product_final = np.logical_and(np.hstack((A, final_column[j])), np.vstack((B, candidate_row)))
            candidate_final_cover[j] = w_p * np.sum(np.sum(M[product_final])) - w_m * np.sum(np.sum(negM[product_final]))

        # find the best candidate and add them to A and B
        index = np.argmax(candidate_final_cover)
        A = np.hstack((A, final_column[index]))
        B = np.vstack((B, association_matrix[index, :]))

    return A, B
