def maxProfit(prices):

    index = 2
    curDiff = prices[1] - prices[0]
    holder = curDiff
    maxDifference = 0

    while index <= len(prices) - 1:
        diff = prices[index] - prices[index-1]
        curDiff = max(curDiff+diff, diff)
        if curDiff > maxDifference:
            maxDifference = curDiff

        index += 1

    maxDifference = max(maxDifference,holder)
    return maxDifference

prices = [1,5,8,2]

print(maxProfit(prices))