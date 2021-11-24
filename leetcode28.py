def strStr(haystack,needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    needleLength = len(needle)

    index = 0
    while index < len(haystack):
        if haystack[index] == needle[0]:
            if len(needle) == 1:
                return index
            elif haystack[index:index+needleLength] == needle:
                return index
        index += 1

    return -1

hayStack= "aaaa"
needle = "bbd"


ans = strStr(hayStack,needle)
print(ans)