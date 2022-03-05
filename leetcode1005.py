def largestSumAfterKNegations(nums,k):
    negativeNum = []
    total = 0
    positiveNum = []

    for num in nums:
        if num <= 0:
            negativeNum.append(num)
        else:
            positiveNum.append(num)

    positiveNum.sort()
    negativeNum.sort()
    print(positiveNum)
    print(negativeNum)
    if len(negativeNum) == 0:
        if k % 2 == 0:
            return sum(positiveNum)
        else:
            return -1 * positiveNum[0] + sum(positiveNum[1:])

    # k > len(change smallest to postive)
    if k <= len(negativeNum):
        for num in negativeNum:
            if k >= 1:
                total += num * -1
                k -= 1
            else:
                total += num
        return total + sum(positiveNum)

    else:
        k -= len(negativeNum)
        k %= 2
        if k == 1:
            if len(positiveNum) != 0:
                if abs(positiveNum[0]) > abs(negativeNum[-1]):
                    return sum(positiveNum) + sum(negativeNum) *-1 + negativeNum[-1]*2
                else:
                    return sum(positiveNum[1:])+sum(negativeNum) *-1 + -1*positiveNum[0]
            else:
                return sum(negativeNum[:-1]) * -1 + negativeNum[-1]
        else:
            return sum(positiveNum)+sum(negativeNum)*-1
    # k = len
    # k < len


nums = [-4,-2,-3]
k = 4
print(largestSumAfterKNegations(nums,k))