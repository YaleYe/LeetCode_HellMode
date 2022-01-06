def arrayPairSum(nums):
    nums.sort()
    index=1
    ans = 0

    while index<= len(nums)-1:
        ans += min(nums[index],nums[index-1])
        index += 2

    return ans


nums = [1,4,3,2]
print(arrayPairSum(nums))