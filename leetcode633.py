def judgeSquareSum(c):

    left = 0
    right = int(c**0.5) + 1
    while left <= right:
        val = left ** 2 + right ** 2
        if val == c:
            return True
        if val < c:
            left += 1
        if val > c:
            right -= 1

    return False

ans = judgeSquareSum(11)
print(ans)
