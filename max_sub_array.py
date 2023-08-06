def max_sub_array(A):
    """
    Compute the maximum subarray of an array A.

    Input: array A
    Output: array with start and end index of the maximum subarray
    """

    n = len(A)    
    max_ending_here = A[0]
    max_so_far = A[0]
    begin = 0
    ending = 0

    for i in range(1, n):
        a = A[i]
        b = max_ending_here + A[i]
        max_ending_here = max(a, b)

        if max_ending_here >= max_so_far:
            ending = i
            max_so_far = max_ending_here

        if max_so_far == A[i]:
            begin = i
            ending = i

    return [begin, ending]          