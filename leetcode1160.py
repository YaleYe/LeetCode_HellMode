import collections


def countCharacters(words,chars):
    dict = collections.Counter(chars)
    ret = 0
    for word in words:
        flag = True
        w = collections.Counter(word)
        for key in w.keys():
            if key in dict and dict[key] >= w[key]:
                continue
            else:
                flag = False

        if flag:
            ret += len(word)


    return ret

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

print(countCharacters(words,chars))
