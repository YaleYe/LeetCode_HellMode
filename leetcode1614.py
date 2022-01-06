def maxDeath(s):
    maxLength = 0
    stack = []
    for char in s:
        if char == "(":
            stack.append("(")
            maxLength = max(len(stack), maxLength)

        if char == ")":
            stack.pop()

    return maxLength


s = "(1)+((2))+(((3)))"
print(maxDeath(s))