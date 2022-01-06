import collections


def isSubsequence(s,t):

    
    sIndex = 0
    tIndex = 0

    while tIndex <= len(t) - 1:
        if t[tIndex] == s[sIndex]:
            sIndex += 1
            tIndex += 1
            if sIndex == len(s):
                return True
        else:
            tIndex += 1

    return False



s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))