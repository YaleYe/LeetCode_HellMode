def nextPermutation(nums):


    # loop backwards, find the first decending
    for i in range(len(nums)-1,-1,-1):
        if nums[i] > nums[i-1]:
            pivot = i - 1
            break
    print(pivot)
    if pivot == -1:
        return nums[::-1]

    for i in range(len(nums)-1,-1,-1):
        if nums[i] > nums[pivot]:
            print((nums[i]))
            temp = nums[pivot]
            nums[pivot] = nums[i]
            nums[i] = temp
            print(nums)
            break

    nums[pivot+1:] = sorted(nums[pivot+1:])
    return (nums)

nums = [1,3,5,4,3,2,1]
print(nextPermutation(nums))