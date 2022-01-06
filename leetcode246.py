def isStrobogrammatic(self, num: str) -> bool:
    singular = ["0", "1", "8"]
    if len(num) == 1:
        if num not in singular:
            return False

    twinSet = set()
    twinSet.add(("0", "0"))
    twinSet.add(("1", "1"))
    twinSet.add(("6", "9"))
    twinSet.add(("8", "8"))
    twinSet.add(("9", "6"))

    i = 0
    end = len(str(num)) - 1

    while i <= end:
        if (num[i], num[end]) not in twinSet:
            return False
        else:
            i += 1
            end -= 1

    return True