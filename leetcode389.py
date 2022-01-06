from collections import Counter
def findTheDifference(s,t):
    dic = Counter(s+t)
    print(dic)
    for key, value in dic.items():
        if value % 2 !=0:
            return key



s = "ya"
t = "y"
print(findTheDifference(s,t))