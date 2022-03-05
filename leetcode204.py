def countPrimes(n):

    if n <3:
        return 0
    container = [1]*n
    container[1] = 0
    container[0] = 0
    for i in range(3,n):

        if i % 2 == 0:
            container[i-1] = 0
            continue
        if i % 3 == 0 and i !=3:
            container[i-1] = 0
            continue
        if i % 5 == 0 and i != 5:
            container[i-1] = 0
            continue
        if i % 7 == 0 and i != 7:
            container[i-1]  = 0
            continue
    print(container)
    return sum(container)


x = countPrimes(10)
print(x)
