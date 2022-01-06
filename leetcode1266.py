def minTimeToVisitAllPoints(points):
    counter = 0

    index = 1
    while index <= len(points)-1:

        counter += max(abs(points[index-1][0]-points[index][0]),
                   abs(points[index-1][1]-points[index][1]))
        index += 1

    print(counter)

points = [[3,2],[-2,2]]
minTimeToVisitAllPoints(points)