def compareVersion(version1,version2):

    v1 = version1.split(".")
    v2 = version2.split(".")
    print(v1)
    print(v2)

    minLength = min(len(v1),len(v2))

    for i in range(0,minLength):
        v1String = int(str(v1[i]))
        v2String = int(str(v2[i]))

        if v1String != v2String:
            if v1String > v2String:
                return 1
            else:
                return -1
        else:
            continue

    if len(v1) == len(v2):
        return 0

    elif len(v2) > len(v1):
        for s in v2[minLength:]:
            v2String = int(str(s))
            if v2String != 0:
                return -1
            continue
        return 0

    else:
        for s in v1[minLength:]:
            v1String = int(str(s))
            if v1String != 0:
                return 1
            continue
        return 0




version1 = "1.0.1"
version2 = "1"


print(compareVersion(version1,version2))

