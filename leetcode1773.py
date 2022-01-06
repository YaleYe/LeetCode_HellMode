def countMatches(items,rules,ruleValue):

    # type = 1
    # color = 2
    # name =  3
    index = 0
    if rules == "type":
        index = 0
    if rules == "color":
        index = 1
    if rules == "name":
        index = 2

    counter = 0
    for item in items:
        if item[index] == ruleValue:
            counter += 1

    return counter

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(countMatches(items,ruleKey,ruleValue))