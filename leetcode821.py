def shortestToChar(s,c):
    left = [None]*len(s)
    right = [None]*len(s)
    ans = [None]*len(s)

    temp = len(ans)

    for i in range(len(s)):
        if s[i] == c:
            temp = 0
        left[i] = temp
        temp += 1

    j = len(s)-1
    temp2 = len(ans)
    while j >= 0:
        if s[j] == c:
            temp2 = 0
        right[j] = temp2
        temp2 += 1
        j -= 1


    for i in range(0,len(left)):
        ans[i] = min(left[i],right[i])

    print(ans)



s = "loveleetcode"
c = "e"

shortestToChar(s,c)