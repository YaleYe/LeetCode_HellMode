def isArmstrong(n):

    sum = 0

    nString = str(n)
    totalLength = len(nString)

    for i in range(0,totalLength):
        sum += int(nString[i]) ** totalLength

    print(sum)
    return sum == n


n = 123
print(isArmstrong(n))