def findOrder(numCourses, prerequisites):
    # format [toTake, required]

    dict = {i: [] for i in range(0, numCourses)}

    for course in prerequisites:
        dict[course[1]].append(course[0])

    # visited
    # circle

    visited = set()
    circle = set()
    ans = []
    print(dict)

    def dfs(course):
        if course in visited:
            return True
        if course in circle:
            return False
        circle.add(course)

        for c in dict[course]:
            if dfs(c) == False:
                return False
        circle.remove(course)
        visited.add(course)
        ans.append(course)
        return True

    for i in range(0, numCourses):
        if dfs(i) == False:
            return []
    return ans


num = 1
pre = []

print(findOrder(num, pre))
