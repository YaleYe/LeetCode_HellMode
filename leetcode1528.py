def restoreString(s,indices):
    stringSotre = [None] * len(indices)

    index = 0

    while index <= len(s) -1:
        stringSotre[indices[index]] = s[index]
        index += 1

    return ''.join(stringSotre)


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s,indices))