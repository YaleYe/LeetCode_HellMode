def findPoisonedDuration(timeSeries,duration):

    counter = 0
    endTime = -1
    index = 0
    while index <= len(timeSeries) -1:
        if timeSeries[index] >= endTime:
            counter += duration
            endTime = duration+timeSeries[index]
        else:

            addTime = timeSeries[index-1]+duration - timeSeries[index]
            counter = counter + duration - addTime
            endTime = duration + timeSeries[index]
        index += 1
    print(counter)


timeSeries = [1,2]
duration = 2

print(findPoisonedDuration(timeSeries,duration))