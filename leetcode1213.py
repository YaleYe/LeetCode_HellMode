def arraysIntersection(arr1, arr2, arr3):
    arr1Set = set()
    arr2filterd = set()
    arr3Set = set()
    for num in arr1:
        arr1Set.add(num)

    for num in arr2:
        if num in arr1Set:
            arr2filterd.add(num)

    for num in arr3:
        if num in arr2filterd:
            arr3Set.add(num)



    return sorted(list(arr3Set))


arr1 = [197, 418, 523, 876, 1356]
arr2 = [501, 880, 1593, 1710, 1870]
arr3 = [521, 682, 1337, 1395, 1764]
print(arraysIntersection(arr1,arr2,arr3))