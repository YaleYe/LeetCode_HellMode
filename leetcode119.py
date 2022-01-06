def generate(numRows):

    if numRows == 0:
        return [1]

    base = [1,1]

    if numRows == 1:
        return base


    numRows -= 1

    while numRows > 0:

        index = 1
        newRow = [1]
        while index <= len(base)-1:
            newRow.append(base[index-1]+base[index])
            index += 1
        newRow.append(1)
        base = newRow
        numRows -= 1


    return base

print(generate(3))
