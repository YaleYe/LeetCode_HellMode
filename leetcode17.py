def letterCombination(digits):
    if len(digits) == 0:
        return []
    dict = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r', 's'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    }

    possibleCombination = []
    for digit in str(digits):
        print(digit)
        if int(digit) in dict.keys():
            if len(possibleCombination) == 0:
                possibleCombination.append(dict[int(digit)])
                print(possibleCombination)
            else:
                tempAns = possibleCombination[0]
                newAns = []
                for letter in tempAns:
                    for letter2 in dict[int(digit)]:
                        newAns.append(letter+letter2)
                possibleCombination[0] = newAns

    return possibleCombination[0]


digits = ""
ans = letterCombination(digits)
print(ans)


