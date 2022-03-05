import collections


def minAddToMakeValid(s):
    stack = []
    leng = 0
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                leng += 1

    return leng + len(stack)
s = "((("
print(minAddToMakeValid(s))