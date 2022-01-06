def arrangeCoins(n):

    dic = {
        1:1,
        2:3,
        3:6,
    }

    if n < 1:
        return 0
    if n < 3:
        return 1
    if n < 6:
        return 2


    for index in range(3,n+1):
        ans = dic[index-1]+index
        if n < ans:
            return index - 1
        if n == ans:
            return index
        dic[index] = ans



x= arrangeCoins(2)

print(x)