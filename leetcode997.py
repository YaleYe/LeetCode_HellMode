def findJudge(n,trust):

    truster = set()
    trusted = {}

    for i in trust:

        truster.add(i[0])
        if i[1] not in trusted:
            trusted[i[1]] = 1
        else:
            trusted[i[1]] += 1


    for key in trusted.keys():
        if trusted[key] == n-1:
            if key not in truster:
                return key


    return -1

n = 2
trust = [[1, 2]]


print(findJudge(n,trust))
