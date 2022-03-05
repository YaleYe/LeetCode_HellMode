def solution(sourceArray, destinationArray):


    unMatchIndex = [0,len(sourceArray)-1]

    index = 0
    while index <= len(sourceArray)-1:
        if sourceArray[index] != destinationArray[index]:
            unMatchIndex.append(index)


        index += 1
    unMatchIndex.sort()

    if len(unMatchIndex) == 2:
        return [0,0]
    if len(unMatchIndex)-2 == len(destinationArray):
        return [0,0]
    index = 1
    longest = 0
    longIndex = 0

    while index <= len(unMatchIndex)-1:
        diff = unMatchIndex[index] - unMatchIndex[index-1]
        if diff > longest:
            longest = diff
            longIndex = index
        index += 1
    return [longest,longIndex]


sourceArray= [92988800, 80253955, 17396563, 91682092, 77708269, 97587946, 23889892, 20661856, 21013095, 92028000, 17562863, 86804822, 17819093, 97941923, 64955308]
destinationArray= [92988800, 80253955, 17396563, 91682092, 77708229, 97587946, 23889892, 20661866, 21013095, 92928000, 17962863, 86804822, 14819093, 97241923, 62955308]
print(solution(sourceArray,destinationArray))