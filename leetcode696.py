def countBinarySubstrings(s):
    ans = 0
    flag = s[0]

    prev = 0
    now = 0
    for char in s:
        if flag == char:
            now += 1
        else:
            ans += min(prev,now)
            prev = now
            now = 1
            flag = char
    ans += min(prev,now)

    return ans




s = "00110011"
print(countBinarySubstrings(s))


