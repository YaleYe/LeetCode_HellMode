def reverseString(s) -> None:

    left = 0
    right = len(s)-1
    while left <= right:
        lnum = s[left]
        rnum = s[right]
        s[right] = lnum
        s[left] = rnum
        left += 1
        right -= 1

    return s


s = ["h","e","l","l","o"]
print(reverseString(s))

