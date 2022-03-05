
def closingTime(list):
    bestList = [0] * (len(list)+1)
    #[0,0,0,0,0]
    #[Y,Y,Y,Y]

    #[0,1,0,0,0]
    i = 0

    while i <= len(list) -1:
        if list[i] == "Y":
            best = max(bestList[i]+1,bestList[i+1])
            bestList[i+1] = best
        else:
            best = max(bestList[i]-1, bestList[i+1])
            bestList[i+1] = best
        i += 1

    print(bestList)

list = ["Y","Y","Y","Y"]
closingTime(list)