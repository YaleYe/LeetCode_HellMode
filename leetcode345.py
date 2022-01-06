def reverseVowels(s):

    s = list(s)
    left = 0
    right = len(s) - 1

    vowels = set()
    vowels.add("a")
    vowels.add("e")
    vowels.add("i")
    vowels.add("o")
    vowels.add("u")
    vowels.add("A")
    vowels.add("E")
    vowels.add("I")
    vowels.add("O")
    vowels.add("U")

    while left <= right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            tempString = s[left]
            tempString2 = s[right]
            s[left] = tempString2
            s[right] = tempString
            left += 1
            right -= 1
    print(''.join(s))

s = "A man, a plan, a canal: Panama"
reverseVowels(s)

