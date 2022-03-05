def validMountainArray(arr):

    index = 1
    peak = float("-inf")
    # find first peak
    while index <= len(arr)-1:

        if index == len(arr)-1:
            print(index)
            return False
        if arr[index] > arr[index-1]:
            index += 1
            continue
        else:
            peak = arr[index-1]
            break

    print(peak)
    while index <= len(arr)-1:
        if index == len(arr)-1:
            return True

        if arr[index] < peak:
            peak = arr[index]
            index += 1
            print(peak)
            continue
        else:
            return False





arr = [1,3,2]
print(validMountainArray(arr))
