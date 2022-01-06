def largestPerimeter(nums):
    nums.sort(reverse=True)
    rightIndex = 2
    print(nums)

    while rightIndex <= len(nums) - 1:
        num1 = nums[rightIndex-2]
        num2 = nums[rightIndex-1]
        num3 = nums[rightIndex]
        if num1 < num2 + num3:
            return num1+num2+num3
        rightIndex += 1

    return 0



nums = [3,9,2,5,2,19]
ans = largestPerimeter(nums)
print(ans)