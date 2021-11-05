def addToArrayForm(num,k):

    kList = list(str(k))

    if len(num) > len(str(k)):
        kList = list("0" * (len(num)-len(str(k))) + str(k))
    else:
        numList = list("0"* (len(str(k)) - len(num))) + num
        num = numList

    kList = kList[::-1]
    num = num [::-1]
    ansList = []
    carry = 0
    for digit in range(0,len(kList)):
        summ = int(kList[digit]) + int(num[digit]) + carry
        carry = summ // 10
        leftover = summ % 10
        ansList.append(leftover)

    if carry:
        ansList.append(carry)

    ansList = ansList[::-1]
    return ansList

num = [1,2,0,0,0]
k = 34

ans = addToArrayForm(num,k)
print(ans)
