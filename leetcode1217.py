def minCostToMoveChips(position):
    oddSum = 0
    evenSum = 0

    for pos in position:
        if pos % 2 == 0:
            evenSum += 1
        else:
            oddSum += 1

    return min(oddSum,evenSum)



pos = [1,1000000000]

print(minCostToMoveChips(pos))