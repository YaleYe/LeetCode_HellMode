import collections


def canPermutePalindrome(s):
    dic = collections.Counter(s)
    counter = 0
    for key in dic.keys():
        if dic[key] % 2 != 0:
            counter += 1

        if counter > 1:
            return False

    return True


s = "code"
ans = canPermutePalindrome(s)

print(ans)