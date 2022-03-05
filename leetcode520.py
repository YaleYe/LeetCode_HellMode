def detectCapitalUse(word):

    # 1. all lower
    # 2. all higher
    # 3. Index0: Cap, index1: low
    if len(word) in [0,1]:
        return True

    if word[0].islower():
        if word[1:].lower() == word[1:]:
            return True
    else:
        if word[1:].lower() == word[1:]:
            return True
        if word[1:].upper() == word[1:]:
            return True
    return False


word = "Ass"

print(detectCapitalUse(word))