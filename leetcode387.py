def firstUniqChar(s: str) -> int:

    dic = {

    }

    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    candidates = set()
    for key in dic.keys():
        if dic[key] == 1:
            candidates.add(key)

    if len(candidates) == 0:
        return -1

    index = 0
    for char in s:
        if char in candidates:
            return index

        index += 1

s = "loveleetcode"
print(firstUniqChar(s))