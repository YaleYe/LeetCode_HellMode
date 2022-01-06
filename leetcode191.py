def hammingWeight(n) -> int:
    counter = 0
    for letter in str(n):
        if letter == "1":
            counter += 1

    return counter


n = "00000000000000000000000000001011"


print(hammingWeight(n))
