import numpy as np
import numpy.matlib

def asso2(M, k, tau, w_p, w_m):
    m, n = M.shape
    A = np.zeros((m, n), dtype=bool)
    B = np.zeros((n, m), dtype=bool)
    negM = ~M

    # association matrix
    association_matrix = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(n):
            if np.sum(np.multiply(M[:, i], M[:, j])) / np.sum(M[:, i]) > tau:
                association_matrix[i, j] = 1


    # Asso algorithm
    for factor in range(k):
        candidate_final_cover = np.zeros((1,m), dtype=bool)
        final_column = np.empty((n, m), dtype=bool)
        print(factor)

        product = np.dot(np.hstack((A, np.zeros((m, 1), dtype=bool))), np.vstack((B, np.zeros((1, n), dtype=bool))))
        product = product.astype(bool)

        cover_base = w_p * np.sum(np.sum(M[product])) - w_m * np.sum(np.sum(negM[product]))

        # loop over all candidate (rows in association matrix)
        for j in range(association_matrix.shape[0]):
            final_column[j] = np.zeros(m, dtype=bool)
            candidate_row = association_matrix[j, :]

            # vectorized loop over all rows
            changed = np.logical_and(~product, numpy.matlib.repmat(candidate_row, m, 1))  # check only changed values
            
            covered_by_change = np.logical_and(M, changed)
            overcovered_by_change = np.logical_and(negM, changed)
            cover_aktualni = cover_base + w_p * np.sum(covered_by_change, axis=1) - w_m * np.sum(overcovered_by_change, axis=1)
            
            final_column[j][cover_base < cover_aktualni] = 1 #kde plati < tam je 1

            product_final = np.dot(np.column_stack((A, final_column[j])), np.row_stack((B, candidate_row)))
            product_final = product_final.astype(bool)
            candidate_final_cover[:,j] = w_p * np.sum(np.sum(M[product_final])) - w_m * np.sum(np.sum(negM[product_final]))

        # find the best candidate and add them to A and B
        index = np.argmax(candidate_final_cover)
        A = np.column_stack((A, final_column[index]))
        B = np.row_stack((B, association_matrix[index, :]))

    return A, B

M = np.array([[0,0,1,0],[1,1,1,1],[0,1,1,1],[0,1,1,0]])
A, B = asso2(M, 3, 0.9, 1, 1)
print(A)
print(B)