def canAttendMeetings(intervals):
    newIntervals = sorted(intervals, key=lambda row: row[0], reverse=False)
    index = 1
    while index < len(intervals):
        if newIntervals[index-1][1] < newIntervals[index][0]:
            index += 1
        else:
            return False
    return True
intervals = [[7,10],[2,4]]
print(canAttendMeetings(intervals))