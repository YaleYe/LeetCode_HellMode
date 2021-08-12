
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longString = ""
    for i in range(0,len(s)):
        endIndex = len(s)
        while isParlin(s[i:endIndex]) is False:
            endIndex -= 1
        else:
            if len(s[i:endIndex]) >= len(longString):
                longString = s[i:endIndex]
    return longString

def isParlin(s):
    halfLength = int(len(s) / 2)
    #print(halfLength)
    index = 0
    endIndex = len(s) -1
    while index < halfLength:
        if s[index] != s[endIndex]:
            return False
        endIndex -= 1
        index += 1
    return True




s = "babbab"
sl = "bb"
se = "bbbb"
x = "cbbd"


z = longestPalindrome(s)
print(z)

# "bab"

#"cbbd"
#"bb"

#ac
#a