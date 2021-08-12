def twoSum(nums,target):
    for index in range(0, len(nums)):
        for secondIndex in range(index+1,len(nums)):
            if nums[index] + nums[secondIndex] == target:
                return [index,secondIndex]

