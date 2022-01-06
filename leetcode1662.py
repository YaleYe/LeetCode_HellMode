def arrayStringsAreEqual(word1,word2):

    return "".join(word1) == "".join(word2)

word1 = ["a", "cb"]
word2 = ["ab", "c"]

print(arrayStringsAreEqual(word1,word2))