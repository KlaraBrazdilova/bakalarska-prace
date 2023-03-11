from numpy import matrix, sort, zeros, array, intersect1d, append, transpose
from functools import reduce

#funkce arrow univerzální, jenom pro down volám klasicky a pro up s transponovanou maticí?
def arrow(U:matrix, indexes):
    foo, far = [], array([], dtype=int)
    indexes = sort(indexes)

    for col in indexes:
        for row in range(U.shape[0]):
            if U[row,col] == 1:
                far = append(far, row)   
        foo.append(far)
        far = array([], dtype=int)

    if len(foo) == 0:
        return array([], dtype=int)
    
    if len(foo) == 1:
        return foo[0]
    
    return reduce(intersect1d, foo)    

def down_arrow(U:matrix, indexes):
    rows, pom = [], array([], dtype=int)
    indexes = sort(indexes)

    for col in indexes:
        for row in range(U.shape[0]):
            if U[row,col] == 1:
                pom = append(pom, row)   
        rows.append(pom)
        pom = array([], dtype=int)
    #v rows je pole poli ktere obsahujou indexy radku ktere obsahuji 1
    # potrebuji průnik (intersection) techto poli

    if len(rows) == 0:
        return array([], dtype=int)
    
    if len(rows) == 1:
        return rows[0]
    
    return reduce(intersect1d, rows)

def up_arrow(U:matrix, indexes):
    cols, pom = [], array([], dtype=int)
    indexes = sort(indexes)

    for row in indexes:
        for col in range(U.shape[1]):
            if U[row,col] == 1:
                pom = append(pom, col)
        cols.append(pom)
        pom = array([], dtype=int)

    if len(cols) == 0:
        return array([], dtype=int)
    if len(cols) == 1:
        return cols[0]    
    return reduce(intersect1d, cols)    

def my_struct(cols, ups, downs, cover):
    return {'cols': cols, 'ups': ups,'downs': downs ,'cover': cover}

def GreConD(I:matrix):
    U = I.copy()
    width = I.shape[0]
    height = I.shape[1]
    A = zeros((height, width))
    B = zeros((width, height))
    best = my_struct([],[],[],0)
    a = 0
    while U.any():
        for i in range(width):
            downs = arrow(U, [i]) #down_arrow(U,[i])
            ups = arrow(transpose(U), downs) #up_arrow(U,downs)
            if len(downs)*len(ups) >= best['cover']:
                best = my_struct([i],ups,downs,len(downs)*len(ups))
        
        first_best = best['cols'][0]
        for i in range(width):
            if i != first_best:
                downs = arrow(U,[i,first_best]) #down_arrow(U,[i,first_best])
                ups = arrow(transpose(U), downs) #up_arrow(U,downs)
                if len(downs)*len(ups) >= best['cover']:
                    best = my_struct([first_best, i],ups,downs,len(downs)*len(ups))

        for row in best['downs']:
            A[row,a] = 1

        for col in best['ups']:
            B[a,col] = 1

        for col in best['ups']:
            for row in best['downs']:
                U[row,col] = 0
        print(best['cover'], best['cols'], best['ups'], best['downs'])
        print(f"iterace {a} vypadá {U}")
        a += 1
        best = my_struct([],[],[],0)


matrix_test = matrix([[0,0,1,1,1,1],[0,1,0,1,0,1],[1,1,0,0,1,1],[1,0,0,1,1,0],[0,0,0,1,1,0]])
#print(matrix_test)
#print(up_arrow(matrix_test,[0,1,3,4]))
GreConD(matrix_test)
