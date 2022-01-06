def peakIndexInMountainArray(arr):
    index = 1
    while index <= len(arr)-2:
        if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
            print(index)
            return index

arr = [0, 10, 5, 2]
peakIndexInMountainArray(arr)