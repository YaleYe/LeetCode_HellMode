def countSegments(s):
    list = s.split(" ")

    counter = 0
    print(list)
    for c in list:
        if c != "":
            counter += 1
    return counter




s = "             "
print(countSegments(s))