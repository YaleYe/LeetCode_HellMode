import collections


def hammingDistance(x,y):
    difference = str(bin(x^y))

    dic = collections.Counter(difference)

    print(dic["1"])


x = 3
y = 2
hammingDistance(x,y)