import math


def diletation(matrix, mask):
    """
    Dilatation of a matrix with a mask.

    Input: binary matrix M, binary mask
    Output: dilated matrix M
    """

    matrix_copy = matrix.copy()
    m, n = matrix.shape
    mask_m, mask_n = mask.shape
    size = math.floor(mask_m/2)

    for i in range(m):
        for j in range(n):
            for k in range(mask_m):
                for l in range(mask_n):
                    try:
                        if mask[k, l] and matrix[i-size+k, j-size+l]:
                            matrix_copy[i, j] = 1
                            break
                    except IndexError:
                        pass
                    
    return matrix_copy  