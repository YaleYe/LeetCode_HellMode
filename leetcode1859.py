def sortSentence(s):
    s = s.split()
    map = dict()
    ans = ""
    for string in s:
        map[string[-1]] = string[:-1]

    for key in sorted(map):
        ans+=map[key]+" "
    return ans[:-1]
s = "is2 sentence4 This1 a3"

ans = sortSentence(s)
print(ans)
