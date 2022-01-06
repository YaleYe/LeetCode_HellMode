def minRemoveToMakeValid(s):

    sList = list(s)
    stack = []

    for i in range(0,len(sList)):
        if sList[i] == "(":
            stack.append(i)
        if sList[i] == ")":
            if not stack:

                sList[i] = ""
            else:
                stack.pop()

    for index in stack:
        sList[index] = ""


    return ''.join(sList)


s = "a)b(c)d"
print(minRemoveToMakeValid(s))