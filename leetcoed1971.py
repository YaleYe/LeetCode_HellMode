def validPath(n, edges, start, end):

    #start -> finish
    dict = {

    }


    for edge in edges:
        key = edge[0]
        val = edge[1]
        if key not in dict:
            dict[key] = [val]
        else:
            dict[key].append(val)

    startPoint = []
    for key in dict.keys():
        if key == start:
            startPoint = dict[key]

    counter = 0
    while startPoint:
        startingKey = startPoint.pop()
        for key in dict.keys():
            if startingKey == key:
                if end in dict[startingKey]:
                    return True
                else:
                    if counter > n:
                        return False
                    counter += 1
                    startPoint.append((dict[startingKey]))
    return False
n = 6
edges = [[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]]
start = 0
end = 5
print(validPath(n,edges,start,end))