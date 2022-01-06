def topKFrequent(nums,k):
    dic = {}

    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    ans = []
    for key in dic.keys():
        ans.append([key,dic[key]])

    sortedList = sorted(ans,key=lambda x: x[1], reverse = True)

    ans = []

    for i in range(0,k):
        ans.append(sortedList[i][0])
    print(ans)
nums = [3,1,1,1,2,2]
topKFrequent(nums,2)