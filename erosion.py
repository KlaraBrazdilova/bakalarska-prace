import math


def erosion(matrix, mask):
    """
    Erosion of a matrix with a mask.

    input: binary matrix M, binary mask
    output: eroded matrix M
    """

    matrix_copy = matrix.copy()
    m, n = matrix.shape
    mask_m, mask_n = mask.shape
    size = math.floor(mask_m/2)
    mask_ones = 5

    for i in range(m):
        for j in range(n):
            count = 0
            for k in range(mask_m):
                for l in range(mask_n):
                    try:
                        if mask[k, l] and not matrix[i-size+k, j-size+l]:                        
                            matrix_copy[i, j] = 0
                            break
                        else:
                            count += 1
                    except IndexError:
                        pass

            if count == mask_ones:
                matrix_copy[i, j] = 1  

    return matrix_copy 