def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxlength = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    for initIndex in range(0,len(s)):
        length = 0
        for secondIndex in range(initIndex,len(s)):
            if s[secondIndex] not in s[initIndex:secondIndex]:
                length += 1
            else:
                break
        maxlength = max(maxlength,length)
    return (maxlength)


s =  "bbbb"
#output = 3

x = lengthOfLongestSubstring(s)
print(x)