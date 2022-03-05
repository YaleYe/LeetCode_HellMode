def reverseBetween(numList,left,right):
    numList[left-1:right] = numList[left-1:right][::-1]

    print(numList)


numList = [3,5]
left = 1
right = 2

reverseBetween(numList,left,right)

