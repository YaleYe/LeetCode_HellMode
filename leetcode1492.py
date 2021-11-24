def kthFactor(n,k):
    for i in range(0,n+1):
        if i % k == 0:
            k -= 1
            if k == 0:
                return i

    return -1


n = 12
k = 3
print(kthFactor(n,k))