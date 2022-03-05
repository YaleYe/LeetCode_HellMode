from copy import deepcopy
def sumSubarrayMins(arr):


    ret = 0

    def createArray(curArray,index,ret):
        curA = curArray.copy()
        curA.append(index)
        ret += min(curA)
        if index <= len(curArray)-1:
            createArray(curA, index + 1, ret)
        curA.pop()
        ret += min(curA)
        if index <= len(curArray) - 1:
            createArray(curA,index+1,ret)

    createArray(arr,0,ret)
    print(ret)

arr = [3,1,2,4]

sumSubarrayMins(arr)
