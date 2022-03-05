import collections


def buddyStrings(s,goal):

    if len(s) != len(goal):
        return False
    if s == goal:
        dict = collections.Counter(s)
        for key in dict.keys():
            if dict[key] >= 2:
                return True

    index = 0
    tempDiff = []
    goalDiff = []
    while index <= len(s) -1:
        if s[index] != goal[index]:
            tempDiff.append(s[index])
            goalDiff.append(goal[index])
        index += 1

    if len(tempDiff) == 2 and sorted(tempDiff) == sorted(goalDiff):
        return True
    return False


s="abcaa"
goal = "abcbb"

print(buddyStrings(s,goal))
