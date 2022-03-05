import collections


def titleToNumber(columnTitle):


    # -65
    dict = {}
    for i in range(65,91):
        dict[chr(i)] = i-64

    counter = 0
    ret = 1

    for c in columnTitle[::-1]:
        addSum = dict[c] * 26 ** counter
        ret += addSum
        counter += 1


    return ret-1

print(titleToNumber("ZY"))