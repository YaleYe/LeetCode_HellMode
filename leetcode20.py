def isValid(s):

    dict = {
        "[": "]",
        "(": ")",
        "{": "}",
    }

    list = []

    for char in s:
        # if in key
        if len(list) == 0:
            if char in dict.keys():
                list.append(dict[char])
            else:
                return False
        elif list[-1] == char:
            print("find match")
            list.pop(-1)
        else:
            if char not in dict.keys():
                print(list)
                return False
            else:
                list.append(dict[char])

    print(list)

    if len(list) == 0:
        return True

    return False

s="(){}}{"

ans = isValid(s)
print(ans)