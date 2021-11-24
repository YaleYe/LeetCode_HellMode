def findOrder(list):
    # format [toTake, required]
    for item in list:
        item.sort()

    list.sort()

    order = []
    for item in list:
        if ite