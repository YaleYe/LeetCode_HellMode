#41
def countConsistentStirngs(allowed,words):
    allow = set(allowed)



    counter = 0

    for word in words:
        for char in word:
            if char not in allow:
                counter += 1
                break

    return len(words) - counter


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

print(countConsistentStirngs(allowed,words))