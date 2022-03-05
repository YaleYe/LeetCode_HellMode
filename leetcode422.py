def validWordSquare(words):

    dualList = [[]*len(words)]

    print(dualList)

    row = 0
    col = 0

    while row <= len(dualList)-1:
        while col <= len(dualList)-1:

            if len(words[row]) <= len(words):
                words[row] += words[row] + ""*len(words)

            if not dualList[row][col]:
                dualList[row][col] = words[row][col]
                dualList[col][row] = words[row][col]
            if words[row][col] != words[row][col] or words[col][row] != words[row][col]:
                return False

    return True


words = ["abcd", "bnrt", "crmy", "dtye"]
print(validWordSquare(words))