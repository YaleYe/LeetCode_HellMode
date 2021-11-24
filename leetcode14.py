def longestCommonPrefix(strs):

    shortest = len(strs[0])
    for string in strs:
        shortest = min(shortest,len(string))

    matching = ""
    for index in range(0,shortest):
        firstChar = ""
        for string in strs:
            if len(firstChar) == 0:
                firstChar = string[index]
            if string[index] != firstChar:
                return matching
        matching += firstChar
        print(index)
    return matching


strs = ["flower", "flow", "flight"]
ans = longestCommonPrefix(strs)
print(ans)