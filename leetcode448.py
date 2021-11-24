def findDisappearedNumbers(nums):
    numSet = set()
    for i in range(1,len(nums)+1):
        numSet.add(i)
    print(numSet)
    for num in nums:
        if num in numSet:
            numSet.remove(num)

    ans = []

    for item in numSet:
        ans.append(item)

    print(ans)


nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]



findDisappearedNumbers(nums)