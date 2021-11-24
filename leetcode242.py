def isAnagram(s,t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    return s == t
