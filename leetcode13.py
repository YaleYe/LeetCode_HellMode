def intToRoman(num):
    ROMAN_TO_INTEGER = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    index = 0
    sum = 0
    prev = 0
    while index < len(num) :
        cur = ROMAN_TO_INTEGER[num[index]]
        print("prev: " + str(prev))
        print("cur: "+str(ROMAN_TO_INTEGER[num[index]]))
        # start
        if prev == 0:
            prev = cur

        else:
            if prev < cur:
                sum -= prev
                prev = cur
            elif prev >= cur:
                sum += prev
                prev = cur

        index += 1

    print("presum")
    print(sum)
    print(ROMAN_TO_INTEGER[num[-1]])
    sum += ROMAN_TO_INTEGER[num[-1]]

    return sum




s = "MCMXCIV"
ans = intToRoman(s)
print(ans)
