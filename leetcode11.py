def maxArea(height):
    maxArea = 0
    leftPointer = 0
    rightPointer = len(height) -1
    while leftPointer < rightPointer:
        length = rightPointer - leftPointer
        recHeight = min(height[rightPointer], height[leftPointer])
        area = length*recHeight
        maxArea = max(maxArea, area)
        if height[rightPointer] >= height[leftPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return maxArea

height = [1,1]
area = maxArea(height)
print(area)