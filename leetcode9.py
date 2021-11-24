def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    stringLen = len(x)/2 +1
    index = 1
    while (index < stringLen):
        if x[index-1] != x[-1*index]:
            return False
        index += 1

    return True




x = 101
ans = isPalindrome(x)
print(ans)