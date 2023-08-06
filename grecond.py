import copy
from numpy import matrix, sort, zeros, array, intersect1d, append
import numpy as np
from functools import reduce


def down_arrow(U: matrix, indexes):
    rows, pom = [], array([], dtype=int)
    indexes = sort(indexes)

    for col in indexes:
        for row in range(U.shape[0]):
            if U[row, col] == 1:
                pom = append(pom, row)
        rows.append(pom)
        pom = array([], dtype=int)

    if len(rows) == 0:
        return array([], dtype=int)

    if len(rows) == 1:
        return rows[0]

    return reduce(intersect1d, rows)


def up_arrow(U: matrix, indexes):
    cols, pom = [], array([], dtype=int)
    indexes = sort(indexes)

    for row in indexes:
        for col in range(U.shape[1]):
            if U[row, col] == 1:
                pom = append(pom, col)
        cols.append(pom)
        pom = array([], dtype=int)

    if len(cols) == 0:
        return array([], dtype=int)

    if len(cols) == 1:
        return cols[0]

    return reduce(intersect1d, cols)


def my_struct(cols=[], ups=[], downs=[], cover=0):
    return {'cols': cols, 'ups': ups, 'downs': downs, 'cover': cover}

def overlamp(U: matrix, ups, downs):
    overlamp = 0
    for i in downs:
        for y in ups:
            if U[i, y]:
                overlamp += 1

    return overlamp        
 
def GreConD(I: matrix):
    U = copy.deepcopy(I)
    (height, width) = I.shape
    A = zeros((height,0))
    B = zeros((0,width))
    best = my_struct()
    factors = 0
    tran_i = copy.deepcopy(I).transpose()
    
    while U.any():
        indexes = [i for i, column in enumerate(tran_i) if column.any()] 

        while not len(best['cols']) == width and indexes:
            new_best = my_struct()
            for i in indexes:
                downs = down_arrow(I, best['cols'] + [i])
                ups = up_arrow(I, downs)
                cover = overlamp(U, ups, downs)
                if cover > new_best['cover']:
                    new_best = my_struct(
                        best['cols'] + [i], ups, downs, cover)

            if new_best['cover'] < best['cover']:
                break

            best = new_best
            [indexes.remove(id) for id, val in enumerate(best['ups']) if val and id in indexes]


        new_col = zeros((height, 1))
        new_row = zeros((1, width))

        for col in best['ups']: 
            for row in best['downs']:
                U[row, col] = 0
                tran_i[col, row] = 0
                new_col[row, 0] = 1

            new_row[0, col] = 1   

        A = np.append(A, new_col, axis=1) #exis=1 add column
        B = np.append(B, new_row, axis=0) #exis=0 add row

        factors += 1
        best = my_struct([], [], [], 0)
        
    return A, B, factors
