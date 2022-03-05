def sequentialDigits(low,high):
    digit = ["1","2","3","4","5","6","7","8","9"]

    minDigit = len(str(low))

    ans = []

    leftIndex = 0
    rightIndex = leftIndex + minDigit

    while leftIndex <= len(digit):
        while rightIndex <= len(digit):
            num = int(''.join(digit[leftIndex:rightIndex]))
            if low <= num <= high:
                ans.append(num)
            rightIndex += 1
        leftIndex += 1
        rightIndex = leftIndex+minDigit
    return sorted(ans)


print(sequentialDigits(100,300))
