def decodeString(s):

    stack = []
    number = 0
    answer = ""
    for char in s:
        if char.isalpha():
            answer += char
        if char.isdigit():
            number = number * 10 + int(char)

        if char == "[":
            stack.append(answer)
            stack.append(number)
            answer = ""
            number = 0
        if char == "]":
            num = stack.pop()
            prevString = stack.pop()
            answer = prevString + answer*num

    print(answer)


s = "100[leetcode]"
decodeString(s)