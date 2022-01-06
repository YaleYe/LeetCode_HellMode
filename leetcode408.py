def validWordAbbreviation(word,abbr):

    i = 0
    j = 0 # abbr

    while j < len(abbr) and i < len(word):
        if abbr[j].isalnum():
            if word[i] != abbr[j]:
                return False

            i += 1
            j += 1

        else:
            if abbr[j] ==  "0":
                return False

            temp = 0
            while i

word ="hi"
abbr = "hi1"

print(validWordAbbreviation(word,abbr))