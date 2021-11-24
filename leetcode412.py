def fizzbuzz(n):
    ansList = []
    for x in range(1,n+1):
        if x % 3 == 0 and x % 5 == 0:
            ansList.append("FizzBuzz")
        elif x % 3 == 0:
            ansList.append("Fizz")
        elif x % 5 == 0:
            ansList.append("Buzz")
        else:
            ansList.append(str(x))
    return ansList

x = 3
z = fizzbuzz(x)
print(z)