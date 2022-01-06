def mostWordsFound(sentences):

    maxLength = 0

    for sentence in sentences:
        if len(sentence.split(" ")) > maxLength:
            maxLength = len(sentence.split(" "))

    return maxLength


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

print(mostWordsFound(sentences))