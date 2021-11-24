def minMeetingRooms(intervals):
    start = sorted([x[0] for x in intervals])
    end = sorted([x[1] for x in intervals])

    leftPointer = 0
    rightPointer = 0
    counter = 0
    ans = 0
    while leftPointer <= len(start)-1:
        if start[leftPointer] <= end[rightPointer]:
            leftPointer += 1
            counter += 1
        else:
            counter -= 1
            rightPointer += 1
        ans = max(ans,counter)
    print(ans)

intervals = [[13,15],[1,13]]
minMeetingRooms(intervals)
