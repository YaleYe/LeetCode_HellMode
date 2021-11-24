def maxProfit(inventory,orders):
    inventory.sort(reverse=True)

    index = 0
    cost = 0

    while orders > 0:

        if index == len(inventory) - 1:
            if orders > len(inventory):
                cost += len(inventory) * inventory[-1]
                inventory[-1] -= 1
                orders -= len(inventory)
            else:
                cost += orders * inventory[-1]
                return cost

        elif inventory[index] > inventory[index + 1]:
            cost += inventory[index] * (index + 1)
            orders -= (index + 1)
            inventory[index] -= 1

        else:
            index += 1
    return cost

inventory =  [1000000000]
order = 1000000000
ans = maxProfit(inventory,order)
print(ans)
