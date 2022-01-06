def canAttendMeetings(intervals):
    newInterval = sorted(intervals)

    index = 0

    while index < len(intervals) -1:
        if newInterval[index][1] <= newInterval[index+1][0]:
            index += 1
        else:
            return False
    return True
intervals = [[13,15],[1,13]]
print(canAttendMeetings(intervals))