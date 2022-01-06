def findRestaurant(list1, list2):
    dict = {}

    existed = set()

    index = 0
    for item in list1:
        index += 1
        if item in dict.keys():
            dict[item] += index
            existed.add(item)

        else:
            dict[item] = index

    index = 0
    for item in list2:
        index += 1
        if item in dict.keys():
            dict[item] += index
            existed.add(item)

        else:
            dict[item] = index


    newDict = {}
    for item in existed:
        newDict[item] = dict[item]

    max = len(list1) + len(list2)


    for key in newDict.keys():
        if newDict[key] < max:
            max = newDict[key]

    ans = []
    for key in newDict.keys():
        if newDict[key] == max:
            ans.append(key)
    return ans

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

print(findRestaurant(list1,list2))

