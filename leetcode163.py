def findMissingRanges(nums,lower,upper):
    index = 0

    newList = []
    while index <= len(nums) -1:
        if nums[index] <= lower-1 or nums[index] >= upper+1:
            index += 1
        else:
            newList.append(nums[index])
            index += 1


    newList.insert(0,lower-1)
    newList.append(upper+1)

    ret = []

    index = 1

    while index <= len(newList)-1:
        if newList[index] - newList[index-1] == 1:
            index += 1
            continue
        if newList[index] - newList[index-1] == 2:
            ret.append(newList[index] - 1)
            index += 1
        else:
            temp = str(newList[index-1]+1)+"->"+str(newList[index]-1)
            ret.append(temp)
            index += 1


    print(ret)

nums = []
lower = 1
upper = 1

findMissingRanges(nums,lower,upper)