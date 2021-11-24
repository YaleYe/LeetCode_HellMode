def merge(intervals):
    newList = []
    intervals.sort()
    for interval in intervals:
        if len(newList) == 0:
            newList.append(interval)
        if newList[-1][1] >= interval[0]:
            if newList[-1][1] <= interval[1]:
                newList[-1][1] = interval[1]
        else:
            newList.append(interval)

    return newList

intervals =[[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))