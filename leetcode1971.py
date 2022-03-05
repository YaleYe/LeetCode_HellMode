import collections
def validPath(n,edges,start,end):

    edge = {}

    for e in edges:
        if e[0] not in edge:
            edge[e[0]] = [e[1]]
        else:
            edge[e[0]].append(e[1])

        if e[1] not in edge:
            edge[e[1]] = [e[0]]
        else:
            edge[e[1]].append(e[0])

    visited = set()

    queue = collections.deque([start])
    print(edge)
    while queue:
        startIndex = queue.popleft()
        visited.add(startIndex)
        if startIndex in edge.keys():

            for nextIndex in edge[startIndex]:
                if nextIndex == end:
                    return True

                if nextIndex not in visited:
                    queue.append(nextIndex)

    return False


n = 10
edges =[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
start = 7
end = 5

print(validPath(n,edges,start,end))

