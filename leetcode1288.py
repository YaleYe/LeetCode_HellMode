def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda x: (x[0], -1 * x[1]))

    range = [intervals[0]]

    for l,r in intervals[1:]:
        prevL = range[-1][0]
        prevR = range[-1][1]

        if prevL <= l and prevR >= r:

            continue
        range.append([l,r])

    return range


intervals = [[1,4],[3,6],[2,8]]
print(removeCoveredIntervals(intervals)) 