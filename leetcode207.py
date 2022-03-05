def canFinish(numCourses, prerequistites):
    dict = {i: [] for i in range(0, numCourses)}

    for pre in prerequistites:
        dict[pre[1]].append(pre[0])

    circle = set()
    visited = set()

    def dfs(course):

        if course in circle:
            return False

        if course in visited:
            return True
        circle.add(course)
        for c in dict[course]:
            if not dfs(c):
                return False
        visited.add(course)
        circle.remove(course)
        return True

    for course in range(0, numCourses - 1):
        if not dfs(course):
            return False

    return True


num = 2
pre = [[1, 0],[0,1]]

print(canFinish(num, pre))
