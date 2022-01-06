# 10:35-10:38


def firstPalindrome(words):

    def isPar(string):
        i = 0
        end = len(string)-1

        while i < end:
            if string[i] != string[end]:
                return False
            else:
                i += 1
                end -= 1
        return True
    for word in words:
        if isPar(word):
            return word
    return ""

words = ["abc","car","ada","racecar","cool"]

print(firstPalindrome(words))