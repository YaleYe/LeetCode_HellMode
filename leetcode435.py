def findMinArrowShots(points) -> int:
    points = sorted(points, key=lambda a: a[1])

    arrow = 0
    cur = float("inf")


    for point in points:
        if point[0] >= cur:
            cur = point[1]
        else:
            arrow += 1

    return arrow

intervals =[[1,2],[1,2],[1,2]]

print(findMinArrowShots(intervals))