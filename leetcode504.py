def convertToBase7(num):

    string = ""

    flag = False
    if num < 0:
        num = -num
        flag = True

    while num > 0:
        append = num % 7
        string += str(append)
        num //= 7

    if flag:
        return "-"+string[::-1]
    else:
        return string[::-1]








num = -7
print(convertToBase7(num))