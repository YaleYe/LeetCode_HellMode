def findMinArrowShots(points):

    counter = 0

    points = sorted(points,key=lambda a:a[1])
    curStart = -1
    for point in points:

        if point[0] > curStart:
            curStart = point[1]
            counter += 1

    return counter

points =  [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))