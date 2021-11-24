import collections


def findLeastNumOfUniqueInts(arr,k):

    if len(arr) <= k:
        return 0
    numberDict = collections.defaultdict(int)

    for num in arr:
        numberDict[num] += 1

    counterList = []

    for key in numberDict.keys():
        counterList.append(numberDict[key])
    counterList.sort()


    index = 0
    while k >= counterList[index]:
        k -= counterList[index]
        counterList.pop(index)

    return len(counterList)


arr = [1]
k = 1
print(findLeastNumOfUniqueInts(arr,k))