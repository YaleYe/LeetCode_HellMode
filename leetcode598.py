def maxCount(m,n,ops):
    minX = 0
    minY = 0

    for op in ops:
        minX = min(minX,op[0])
        minY = min(minY,op[1])

    return minX*minY


m = 3
n = 3
ops = [[2,2],[3,3]]

print(maxCount(m,n,ops))