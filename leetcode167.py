def twosum(numbers,target):

    leftIndex = 0
    rightIndex = len(numbers) - 1

    while leftIndex < rightIndex:
        print(rightIndex)
        if numbers[leftIndex]+numbers[rightIndex] == target:
            return [leftIndex+1,rightIndex+1]
        if numbers[leftIndex]+numbers[rightIndex] < target:
            leftIndex += 1
        if numbers[leftIndex] + numbers[rightIndex] > target:
            rightIndex -= 1

numbers = [2, 3,4]
target = 6

print(twosum(numbers,target))