def findErrorNums(nums):
    index = 1

    while index <= len(nums)-1:
        if nums[index-1] + 1 != nums[index]:
            return [nums[index],nums[index]+1]
        index += 1


nums = [1,1]
print(findErrorNums(nums))