def mySqrt(x):
    # find range
    left = 0
    right = x

    while left <= right:
        mid = int((left+right)/2)
        if mid*mid < x:
            left = mid + 1
        if mid*mid > x:
            right = mid - 1

        if mid*mid == x:
            return mid

    return left-1

ans = mySqrt(16)
print(ans)