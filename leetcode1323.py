def maximum69Number(num) -> int:

    index = 0
    strList = list(str(num))
    while index <= len(strList) - 1:
        if strList[index] == "6":
            strList[index] = "9"
            break
        index += 1

    print(''.join(strList))


num = 9999

maximum69Number(num)

