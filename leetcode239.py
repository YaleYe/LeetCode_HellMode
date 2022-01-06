def generatePossibleNextMoves(currentState):

    ans = []

    index = 1
    while index <= len(currentState)-1:
        if currentState[index-1]==currentState[index] == "+":
            if index-1 == 0:
                copy = "--" + currentState[2:]
                ans.append(copy)
            elif index+1 == len(currentState):
                ans.append(currentState[:-2]+"--")
                return ans
            else:
                print(index)
                ans.append(currentState[0:index-1]+"--"+currentState[index+1:])
        index += 1

    print(ans)

currentState = "+"
print(generatePossibleNextMoves(currentState))
