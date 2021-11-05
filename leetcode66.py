def plusOne(digits):
    digits[-1] += 1
    digits = digits[::-1]
    carry = 0

    for index in range(0,len(digits)):
        ans = digits[index] + carry
        if ans < 10:
            digits[index] = ans
            return digits[::-1]
        else:
            leftover = ans % 10
            digits[index] = leftover
            carry = ans // 10

    if carry == 1:
        digits.append(1)

    return digits[::-1]

a = [4,2,9,8]
z = plusOne(a)

print(z)