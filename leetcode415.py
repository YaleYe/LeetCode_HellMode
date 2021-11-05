def addStrings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    if len(num1) > len(num2):
        num2 += "0"* (len(num1) - len(num2))
    if len(num2) > len(num1):
        num1 += "0" * (len(num2) - len(num1))

    print(num1)
    print(num2)
    newNumber = ""
    carry = 0
    for i in range(0,len(num1)):
        ans = int(num1[i]) + int(num2[i]) + carry
        leftover = ans % 10
        carry = ans // 10
        newNumber += str(leftover)

    if carry:
        newNumber += carry
    return newNumber[::-1]
num1 = "123"
num2 = "11"
sum = addStrings(num1,num2)
print(sum)