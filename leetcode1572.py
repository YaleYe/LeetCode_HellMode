def diagonalSum(mat):

    ret = 0
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            if i == j or i+j == len(mat)-1:
                ret += mat[i][j]

    return ret

mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
print(diagonalSum(mat))