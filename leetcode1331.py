def arrayRankTransform(arr):
    arr.sort()

    ret = []

    counter = 1
    index = 0
    while index <= len(arr):

        if len(ret) == 0:
            ret.append(counter)

arr = [40,10,20,30]

arrayRankTransform(arr)