def validWordAbbreviation(word,abbr):

    wordIndex = 0
    abbrIndex = 0
    num = 0
    while wordIndex <= len(word)-1 or abbrIndex <= len(abbr) -1:

        while abbr[abbrIndex].isdigit():
           num = num*10 + abbr[abbrIndex]

word ="hi"
abbr = "hi1"

print(validWordAbbreviation(word,abbr))