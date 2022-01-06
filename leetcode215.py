def findKthLargest(nums,k):
    dict = {}
    numList = []

    for num in nums:
        if num not in dict:
            numList.append(num)
            dict[num] = 1

        else:
            dict[num] += 1


    numList.sort(reverse=True)
    print(dict)

    for num in numList:
        if dict[num] >= k:
            return num
        else:
            k -= dict[num]

nums = [3,2,3,1,2,4,5,5,6]
k = 4

print(findKthLargest(nums,k))