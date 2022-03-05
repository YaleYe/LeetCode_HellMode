def solution(n):
    if n == 1:
        return 1
    else:
        return (n-1)**2+n**2


# 5-41
print(solution(5))