def canPlaceFlowers(flowerbed,n):

    flowerbed = [0] + flowerbed + [0]
    index = 2
    maxPlanting = 0


    while index <= len(flowerbed)-1:
        if flowerbed[index-2] == 0 and flowerbed[index-1] == 0 and flowerbed[index] == 0:
            flowerbed[index-1] = 1
            maxPlanting += 1
        index += 1

    print(maxPlanting)

bed = [1]
n = 1
canPlaceFlowers(bed,n )