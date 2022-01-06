def maxProfit(prices):
    holdingPrice= prices[0]
    leftIndex = 0
    rightIndex = leftIndex + 1
    totalProfit = 0
    while rightIndex <= len(prices) - 1:
        # if price is going up
        if prices[leftIndex] < prices[rightIndex]:
            print("made profit" + str(prices[rightIndex] - holdingPrice))
            totalProfit += prices[rightIndex] - holdingPrice
            holdingPrice = prices[rightIndex]
            leftIndex += 1
            rightIndex += 1
        else:
            print("made profit" + str(prices[rightIndex] - holdingPrice))
            leftIndex += 1
            rightIndex += 1
            holdingPrice = prices[leftIndex]


    return totalProfit


prices = [7,1,5,3,6,4]

print(maxProfit(prices))