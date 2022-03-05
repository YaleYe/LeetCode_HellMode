def findAnagrams(s, p):
    p_set = sorted(list(p))

    rightIndex = len(p_set)-1
    answer = []

    while rightIndex <= len(s):
        if s[rightIndex-len(p)] in p_set:
            curString = s[rightIndex-len(p):rightIndex]
            if sorted(list(curString)) == p_set:
                answer.append(rightIndex-len(p))
        rightIndex += 1
    return answer


#s = "abab"
#p = "ab"

##s = "cbaebabacd"
#p = "abc"

s = "ababababab"
p = "aab"
print(findAnagrams(s,p))