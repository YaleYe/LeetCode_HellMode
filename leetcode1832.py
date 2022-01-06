import collections


def checkIfPangram(sentence):

    if len(collections.Counter(sentence)) != 26:
        return False
    return True

sentence = "thequickbrownfoxjumpsoverthelazydog"


print(checkIfPangram(sentence))