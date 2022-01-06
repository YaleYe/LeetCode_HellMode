def numJewelsInStones(jewels,stones):
    a = set(jewels)

    counter = 0
    for s in stones:
        if s in a:
            counter += 1

    return counter