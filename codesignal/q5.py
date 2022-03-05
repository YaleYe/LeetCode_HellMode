def solution(status):

    minNum = min(status)
    maxNum = max(status)

    s = set(status)
    print(maxNum-minNum-len(s) + 1)


status = [0,3]
solution(status)