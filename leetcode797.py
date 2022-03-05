def allPathsSourceTarget(graph):
    ret = []

    dic = {

    }
    index = 0
    while index <= len(graph)-1:
        dic[index] = graph[index]
        index += 1

    stack = [ (0,[0])]

    while stack:
        curNode, curPath = stack.pop()

        #loop
        if curNode == len(graph)-1:
            ret.append(curPath)

        for node in dic[curNode]:

            if node not in curPath:
                tempPath = curPath + [node]
                stack.append((node,tempPath))

    print(dic)
    print(ret)


graph = [[4,3,1],[3,2,4],[3],[4],[]]
allPathsSourceTarget(graph)