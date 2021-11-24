def singleNonDuplicate(nums):
    if len(nums) ==1:
        return nums
    endIndex = 2
    while endIndex<= len(nums):
        if nums[endIndex-2] != nums[endIndex-1] != nums[endIndex]:
            return nums[endIndex-1]
        endIndex += 1

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))