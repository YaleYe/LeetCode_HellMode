def confusingNumber(n):

    dic ={
        6: 9,
        9: 6,
        1: 1,
        0: 0,
        8: 8,
    }
    k = n
    number = 0
    while n > 0:
        if n % 10 not in dic:
            return False
        else:
            number = number * 10 + dic[n % 10]

        n //= 10


    return number != k

n = 11
print(confusingNumber(n))