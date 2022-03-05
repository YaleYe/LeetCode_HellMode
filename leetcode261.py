def validTree(n,edges):

    dict = {i:[] for i in range(0,n)}

    for e in edges:
        dict[e[0]].append(e[1])

    visited =set()

    def dfs(e):

        if e in visited:
            return False

        visited.add(e)
        for e1 in dict[e]:
            if not dfs(e1):
                return False

        return True

    for i in range(0,n):
        if not dfs(i):
            return False

    return True

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(validTree(n,edges))