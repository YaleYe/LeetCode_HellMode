#12:55

def areAlmostEqual(s1,s2):

    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True

    index = 0
    s1List = []
    s2List = []

    while index <= len(s1)-1:
        if s1[index] != s2[index]:
            s2List.append(s2[index])
            s1List.append(s1[index])
        index += 1

    if len(s1List) == 2 and sorted(s1List) == sorted(s2List):
        return True
    return False
