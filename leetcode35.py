def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int((left+right)/2)
        if target < nums[mid]:
            right = mid -1
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid + 1
    return left


nums = [1,3,5,6]
target = 7

ans = searchInsert(nums,target)
print(ans)