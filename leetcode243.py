def shortestDistance(wordsDict, word1,word2) -> int:

    index = 0
    word1Index = []
    word2Index = []
    minDistance = 10000
    for word in wordsDict:
        if word == word1:
            word1Index.append(index)
            if len(word2Index) != 0:
                minDistance = min(minDistance,index-word2Index[-1])
        if word == word2:
            word2Index.append(index)
            if len(word1Index) != 0:
                minDistance = min(minDistance,index-word1Index[-1])

        index += 1

    print(word1Index)
    print(word2Index)
    print(minDistance)


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
shortestDistance(wordsDict,word1,word2)





