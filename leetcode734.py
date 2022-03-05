def areSentencesSimilar(sentence1,sentence2,similarPairs):

    if len(sentence1) != len(sentence2):
        return False



    for i in range(len(sentence1)):
        s1 = [sentence1[i],sentence2[i]]
        s2 = [sentence2[i],sentence1[i]]
        if sentence2[i] == sentence1[i] or s1 in similarPairs or s2 in similarPairs:
            continue
        else:
            return False
    return True

s1 = ["an","extraordinary","meal"]
s2 = ["one","good","dinner"]
s3 = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
print(areSentencesSimilar(s1,s2,s3))