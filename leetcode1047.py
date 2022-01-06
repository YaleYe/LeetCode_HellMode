def removeDuplicates(s):

    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    print(stack)


s = "abbaca"
removeDuplicates(s)