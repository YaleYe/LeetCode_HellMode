def sortedSquares(nums):
    index = 0
    while index <= len(nums)-1:
        val = nums[index]
        nums[index] = val ** 2
        index += 1
    nums.sort()
    return nums

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))