def calculateTime(keyboard,word):

    index = 0

    dic = {

    }

    while index <= len(keyboard)-1:
        dic[keyboard[index]] = index
        index += 1

    prev = 0
    counter = 0
    for char in word:
        counter += abs(dic[char]-prev)
        prev = dic[char]

    print(counter)


keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

print(calculateTime(keyboard,word))