from numpy import matrix, sort, zeros, array, intersect1d, append, transpose
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


def GreConD(I: matrix):
    U = I.copy()
    width = I.shape[0]
    height = I.shape[1]
    A = zeros((height, width))
    B = zeros((width, height))
    best = my_struct()
    a = 0

    while U.any():
        # indexy neprazdnych sloupcu
        indexes = [i for i, column in enumerate(transpose(I)) if column.any()]

        while not len(best['cols']) == width and indexes:
            new_best = my_struct()
            for i in indexes:
                downs = down_arrow(I, best['cols'] + [i])
                ups = up_arrow(I, downs)
                overlamp = len(downs) * len(ups)
                if overlamp >= new_best['cover']:
                    new_best = my_struct(
                        best['cols'] + [i], ups, downs, overlamp)

            if new_best['cover'] < best['cover']:
                break

            best = new_best
            [indexes.remove(id) for id, val in enumerate(
                best['ups']) if val and id in indexes]

        for row in best['downs']:
            A[row, a] = 1

        for col in best['ups']:
            B[a, col] = 1

        for col in best['ups']:
            for row in best['downs']:
                U[row, col] = 0

        for col in best['ups']:
            for row in best['downs']:
                I[row, col] = 0

        print(best['cover'], best['cols'], best['ups'], best['downs'])
        print(f"iterace {a} vypadá {U}")
        a += 1
        best = my_struct([], [], [], 0)


matrix_test = matrix([[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [
                     1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0]])

GreConD(matrix_test)
