def countBits(num):


    return [bin(i).count('1') for i in range(num+1)]

n = 5
x = countBits(n)

print(x)