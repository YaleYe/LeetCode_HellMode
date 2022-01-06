def frequencySort(s):

    dic = {}
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    toList = []

    newDid = {

    }
    for key in dic.keys():

        if dic[key] not in newDid:
            newDid[dic[key]] = [key]
        else:
            newDid[dic[key]].append(key)

    counterList = sorted(list(newDid.keys()),reverse=True)

    retString = ""

    for number in counterList:

        temp = sorted(newDid[number])


        for item in temp:
            retString += item * number

    print(retString)
    print(newDid)
    print(counterList)
    print(toList)


s = "Aabb"
frequencySort(s)