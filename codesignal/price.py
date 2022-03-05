import math


def solution(prices, notes, x):
    diff = 0
    index = 0

    while index <= len(prices)-1:

        note = notes[index].split(" ")
        parse = note[0]

        if parse[0] == "Same":
            continue

        elif note[1] == "higher":
            diffPercent = parse.split(".")[0]
            diff += prices[index] - (prices[index] / (1+int(diffPercent)/100))
            print(diff)

        elif note[1] == "lower":
            diffPercent = parse.split(".")[0]
            # 95/
            diff -= prices[index] - (prices[index] / (1+int(diffPercent)/100))
            print(diff)

        index += 1

    return diff

prices =[110, 95, 70]
notes = ["10.0% higher than in-store",
 "5.0% lower than in-store",
 "Same as in-store"]
print(solution(prices,notes,3))






