def findComplement(num):
    binary = bin(num)[2:]

    newStr = ""
    for char in binary:
        if char == "1":
            newStr += "0"
        else:
            newStr += "1"

    return int(newStr,2)


num = 5
print(findComplement(num))

