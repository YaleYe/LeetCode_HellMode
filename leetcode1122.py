def relativeSortArray(arr1,arr2):

    nonIncluded = []

    dic = {

    }

    for num in arr2:
        dic[num] = 0

    for num in arr1:
        if num in dic.keys():
            dic[num] += 1
        else:
            nonIncluded.append(num)

    print(dic)
    nonIncluded.sort()
    ans = []
    for key in dic.keys():

        for i in range(0,dic[key]):
            ans.append(key)

    ans += nonIncluded
    return ans

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))