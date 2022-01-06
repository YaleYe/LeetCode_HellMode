def frequencySort(nums):
    dic = {

    }
    nums.sort()
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    newDic = dict(sorted(dic.items(), key=lambda x: x[1]))
    verynewDict = {

    }
    for key in newDic:
        # newDIc[key] = appearance
        # key = num
        if newDic[key] not in verynewDict:
            verynewDict[newDic[key]] = [key]
        else:
            verynewDict[newDic[key]].append(key)

    ans = []
    for key in verynewDict:
        verynewDict[key].sort(reverse=True)
        for num in verynewDict[key]:
            for i in range(0,key):
                ans.append(num)

    print(verynewDict)
    print(ans)


nums = [-1,1,-6,4,5,-6,1,4,1]
frequencySort(nums)