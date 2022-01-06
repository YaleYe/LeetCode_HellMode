def toGoatLatin(sentence):

    wordsList = sentence.split(" ")
    print(wordsList)
    ansString = ""
    index = 1
    vowelSet = set()
    vowelSet.add("a")
    vowelSet.add("e")
    vowelSet.add("i")
    vowelSet.add("o")
    vowelSet.add("u")
    for word in wordsList:
        if word[0] in vowelSet:
            ansString += word+"ma"+"a"*index+" "
        else:
            ansString += word[1:]+word[0]+"ma"+"a"*index+" "

        index += 1

    print(ansString)

sentence = "I speak Goat Latin"
toGoatLatin(sentence)