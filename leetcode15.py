def threeSum(nums):
    if len(nums) <= 2:
        return []

    if len(nums) == 3 and nums[0] +nums[1]+nums[2] == 0:
        return [nums]
    nums.sort()

    checkDuplicate = set()
    answer = []

    for initPointer in range(0, len(nums) -3):
        leftPointer = initPointer + 1
        rightPointer = len(nums) - 1

        while leftPointer < rightPointer:
            if nums[initPointer] + nums[leftPointer] + nums[rightPointer] == 0:
                string = str(nums[initPointer]) +" "+str(nums[leftPointer])+" "+str(nums[rightPointer])
                if string not in checkDuplicate:
                    answer.append([nums[initPointer], nums[leftPointer],nums[rightPointer]])
                    checkDuplicate.add(string)
            if nums[initPointer] + nums[leftPointer] + nums[rightPointer] <= 0:
                leftPointer += 1
            else:
                rightPointer -= 1

    return answer

nums = [-3,0,2,1]
ans = threeSum(nums)
print(ans)