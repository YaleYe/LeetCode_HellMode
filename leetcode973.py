def kClosest(points, k):

    ans = []
    # get value, store index
    for point in points:
        value = point[0] ** 2+ point[1] ** 2
        ans.append([point,value])

    ans = sorted(ans, key=lambda x:x[1])


    newAns = []
    for x in range(0,k):
        newAns.append(ans[x][0])
    print(newAns)


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

kClosest(points,k)
