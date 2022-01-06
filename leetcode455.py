def findContentChildren(g,s):
    g.sort()
    s.sort()

    leftIndex = 0
    rightIndex = 0
    print(g)

    while leftIndex <= len(g) -1 and rightIndex <= len(s) - 1:
        if g[leftIndex] <= s[rightIndex]:
            leftIndex += 1
            rightIndex += 1
        else:
            rightIndex += 1

    print(leftIndex)


g = [10,9,8,7]
s = [5,6,7,8]
findContentChildren(g,s)

