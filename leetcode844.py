def backspaceCompare(s,t):

    new_s = []

    for char in s:
        if char == "#":
            if len(new_s) != 0:
                new_s.pop()
        else:
            new_s.append(char)

    new_t = []

    for char in t:
        if char == "#":
            if len(new_t) != 0:
                new_t.pop()

        else:
            new_t.append(char)

    return new_t == new_s


s = "a#c"
t = "b"

print(backspaceCompare(s,t))