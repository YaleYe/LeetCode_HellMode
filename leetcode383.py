def canConstruct(ransomNote, magazine) -> bool:

    dic = {

    }
    for char in magazine:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    for char in ransomNote:
        if char not in dic:
            return False
        else:
            if dic[char] < 1:
                return False
            else:
                dic[char] -= 1

    return True