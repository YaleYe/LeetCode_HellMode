def minimumAbsDifference(arr):
    existed = set()
    answer = []
    minDistance = 10000
    arr.sort()

    index = 1
    while index <= len(arr) - 1:
        diff = arr[index] - arr[index-1]
        comparedString = str(arr[index-1])+"_"+str(arr[index])

        # if smaller found
        if diff < minDistance and comparedString not in existed:
            minDistance = diff
            existed.clear()
            existed.add(comparedString)
            answer = [[arr[index-1],arr[index]]]

        if diff == minDistance and comparedString not in existed:
            existed.add(comparedString)
            answer.append([arr[index-1], arr[index]])

        index += 1
    print(existed)
    print(answer)


arr = [3,8,-10,23,19,-4,-14,27]
minimumAbsDifference(arr)