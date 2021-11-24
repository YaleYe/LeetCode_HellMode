def isPerfectSquare(num):
    left = 0
    right = num

    while left <= right:
        mid = int((left+right)/2)
        if mid*mid > num:
            right = mid - 1
        if mid*mid < num:
            left = mid + 1
        if mid*mid == num:
            return True

    return False


ans = isPerfectSquare(15)
print(ans)