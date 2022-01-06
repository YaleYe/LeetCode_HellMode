def removeVowels(s):

    vowel = set()
    vowel.add("a")
    vowel.add("e")
    vowel.add("i")
    vowel.add("o")
    vowel.add("u")

    newString = ""

    for char in s:
        if char not in vowel:
            newString += char

    print(newString)


s = "leetcodeisacommunityforcoders"
removeVowels(s)