def solution(inputArray):
    i = 1

    ret = float("-inf")

    while i <= len(inputArray)-1:
        ret = max(ret,inputArray[i-1]*inputArray[i])
        i += 1
    return ret

inputArray = [3, 6, -2, -5, 7, 3]
print(solution(inputArray))