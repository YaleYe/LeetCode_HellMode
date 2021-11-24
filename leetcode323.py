def countComponents(n, edges):
    rank = [1] * n
    parent = [x for x in range(0, n)]

    def find(node):
        # node has no parent
        while parent[node] != node:
            node = parent[node]
        return node

    def union(node1,node2):
        p1 = find(node1)
        p2 = find(node2)
        if p1 == p2:
            return 0
        if p2 > p1:
            parent[p1] = p2
            rank[p2] += rank[p1]

        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1


    res = n
    for n1,n2 in edges:
        res -= union(n1,n2)
    return res


n = 5
edges = [[0,1],[1,2],[0,2]]
print(countComponents(n, edges))
