def reverse(x):

    if x > 4294967296 or x < -4294967296:
        return 0
    carry = False
    if x < 0:
        x *= -1
        carry = True

    string = str(x)[::-1]

    while string[0] == "0":
        string = string[1:]


    if carry:
        return -1 * int(string)
    return int(string)


x = 1230100
y = reverse(x)
print(y)

2147483647
2147483648


1534236469