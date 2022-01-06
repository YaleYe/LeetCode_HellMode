def thirdMax(nums):
    existed = set()
    numList = []

    for num in nums:
        if num not in existed:
            existed.add(num)
            numList.append(num)


    numList.sort(reverse=True)

    if len(numList) <= 2:
        return numList[0]

    else:
        return numList[2]


nums = [3,2,1]
print(thirdMax(nums))