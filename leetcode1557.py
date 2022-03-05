def findSmallestSetOfVerticles(n, edges):
    dic = {

    }

    for e in edges:
        if e[0] not in dic:
            dic[e[0]] = [e[1]]
        else:
            dic[e[0]].append(e[1])

    stack = []

    for i in range(0,n):
        stack.append((i,[i]))

    maxList = []

    while stack:
        curNode, curList = stack.pop()

        if curNode in dic.keys():
            for node in dic[curNode]:

                if node not in curList:
                    temp = curList + [node]
                    if len(curList) > len(maxList):
                        maxList = curList
                    stack.append((node,temp))
    print(maxList)

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
findSmallestSetOfVerticles(n,edges)