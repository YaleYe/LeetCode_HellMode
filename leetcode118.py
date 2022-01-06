def generate(numRows):

    base = [[1],[1,1]]

    numRows -= 2

    while numRows > 0:

        index = 1
        newRow = [1]
        prevRow = base[-1]
        while index <= len(prevRow)-1:
            newRow.append(prevRow[index-1]+prevRow[index])
            index += 1
        newRow.append(1)
        base.append(newRow)
        numRows -= 1


    return base

print(generate(5))
