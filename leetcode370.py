def getModifiedArray(length,updates):
    list = [0] * (length+1)

    for update in updates:
        index1 = update[0]
        index2 = update[1]
        change = update[2]
        list[index1] += change
        if index2+1 < len(list):
            list[index2+1] -= change

    for i in range(1,len(list)-1):
        list[i] += list[i-1]

    return list

length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print(getModifiedArray(length,updates))