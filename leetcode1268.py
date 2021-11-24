def suggestedProducts(products,searchWord):
    # newList eachTime
    answer = []
    index = 0
    recentList = products
    while index <= len(searchWord):

        newList = []
        for product in recentList:
            if searchWord[0:index] == product[0:index]:
                newList.append(product)

        newList.sort()
        answer.append(newList[0:3])
        recentList = newList
        index += 1

    print(answer[1:])


#products = ["mobile","mouse","moneypot","monitor","mousepad"]
#searchWord = "mouse"

#products = ["bags","baggage","banner","box","cloths"]
#searchWord = "bags"

#products = ["havana"]
#searchWord = "havana"

products = ["havana"]
searchWord = "tatiana"
suggestedProducts(products,searchWord)