def numberOfMatches(n):
    matches = 0
    while n != 1:

        matches += n - n//2
        n //= 2

    print(matches)
numberOfMatches(14)