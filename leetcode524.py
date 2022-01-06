def findLongestWord(s,dictionary):

    def isSub(s,word):

        index = 0
        for char in s:
            if index == len(word) - 1:
                return True
            if char == word[index]:
                index += 1
        if index != len(word) - 1:
            return False



    maxLength = -1
    candidates = []
    ans = []
    for word in dictionary:
        if isSub(s,word):
            ans.append(word)
            if len(word) == maxLength:
                candidates.append(word)

            elif len(word) > maxLength:
                candidates = [word]
                maxLength = len(word)
    print(candidates)
    print(ans)
    if len(candidates) == 0:
        return ""
    if len(candidates) == 1:
        return candidates[0]
    else:
        return min(candidates)
#print(findLongestWord(word,dic))