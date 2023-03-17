def max_sub_array(A):
    n = len(A)
    max_ending_here = A(1)
    max_so_far = A(1)
    begin = 1
    ending = 1

    for i in range(2, n):
        a = A(i)
        b = max_ending_here + a
        max_ending_here = max(a, b)

        if max_ending_here >= max_so_far:
            ending = i
            max_so_far = max_ending_here

        if max_so_far == a:
            begin = i
            ending = i

    B = [begin, ending]          