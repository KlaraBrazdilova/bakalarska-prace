from math import floor


def square_count(M, size, i, j):
    """Count number of 1s in square of size size around (i,j)."""
    count = 0
    max = floor(size/2)
    for k in range(max+1):
        for l in range(max+1):
            try:
                if M[i + k, j + l]:
                    count += 1
                if M[i - k, j - l]:
                    count += 1 
            except IndexError:
                pass    
    count -= M[i, j]                            
    return count/(size*size)


def square_filter(M, limit, size=3):
    """Filter matrix with square filter of size size."""
    N = M.copy()
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if square_count(M, size, i, j) > limit:
                N[i, j] = 1
            else:
                N[i, j] = 0
    return N
