def multiply(num1,num2):

    ans = 0
    counter = 1
    num2 = list(num2)

    while num2:
        ans += int(num1) * int(num2.pop()) * counter
        counter *= 10

    return ans


num1 = "123"
num2 = "456"

print(multiply(num1,num2))


