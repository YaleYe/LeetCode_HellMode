def removeKdigits(num,k):

    stack = []
    for n in num:
        while stack and stack[-1] >= n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    stack = stack[:len(stack)-k]


    if len(stack) == 0:
        return 0
    else:
        return ''.join(stack)


num = "10200"
k = 1

print(removeKdigits(num,k))