def maximumWealth(accounts) -> int:
    maxMoney = 0
    for account in accounts:
        maxMoney = max(maxMoney,sum(account))

    print(maxMoney)


accounts = [[1,2,3],[3,2,1]]
maximumWealth(accounts)