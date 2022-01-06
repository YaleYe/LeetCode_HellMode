def tribonacci(n: int) -> int:
    dic = {
        0: 0,
        1: 1,
        2: 1,
    }

    for index in range(3, n):
        ans = dic[index-1] + dic[index-2] + dic[index-3]
        dic[index] = ans

    print(dic)


tribonacci(4)
