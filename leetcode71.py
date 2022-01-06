def simplifyPath(path):
    stack = []
    path = path.split("/")

    for item in path:
        print(stack)
        if item == "..":
            if len(stack) != 0:
                stack.pop()

        elif item == "." or item == "":
            continue

        else:
            stack.append(item)

    return "/"+'/'.join(stack)


#path = "/home/"
#path2 = "/a/./b/../../c/"
path3 = "/home//foo/"
#print(simplifyPath(path))
print(simplifyPath(path3))
#print(simplifyPath(path3))

