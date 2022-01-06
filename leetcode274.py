def hIndex(citations):
    citations.sort(reverse=True)
    counter = 0
    for index in range(0,len(citations)):
        if citations[index] > index:
            counter += 1
    print(counter)

citations = [1,3,1]
hIndex(citations)