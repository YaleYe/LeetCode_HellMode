def threeSumClosest(nums,target):

    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
    nums.sort()
    difference = float('inf')
    initIndex = 0
    sum = 0
    while initIndex < len(nums) -1:
        leftIndex = initIndex + 1
        rightIndex = len(nums) -1
        while leftIndex < rightIndex:
            result = target - nums[initIndex] - nums[leftIndex] - nums[rightIndex]
            print("initIndex: "+str(initIndex)+ " left: "+str(leftIndex) + " right:"+str(rightIndex))
            if result == 0:
                return target
            if abs(result) < difference:
                # print(diff)
                difference = abs(result)
                sum = nums[initIndex] + nums[leftIndex] + nums[rightIndex]
            if result < 0:
                rightIndex -= 1
            if result > 0:
                leftIndex += 1
        initIndex += 1

    return sum

nums = [1,1,1,1]
target = -100
ans = threeSumClosest(nums,target)
print(ans)