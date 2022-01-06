def buildArray(nums):

    newNum = [0]*len(nums)

    index = 0
    for num in nums:
        newNum[index] = nums[nums[index]]
        index += 1


    print(newNum)

nums = [0,2,1,5,3,4]
buildArray(nums)