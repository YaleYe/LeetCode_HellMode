def shuffle(nums):

    index = 0
    half = len(nums) // 2

    newNum = []

    while index < half:
        newNum.append(nums[index])
        newNum.append(nums[index+half])
        index += 1

    print(newNum)


nums = [2, 5, 1, 3, 4, 7]
shuffle(nums)