def checkStraightLine(coordinates):
    coordinates.sort()
    x_inc = coordinates[1][0] - coordinates[0][0]
    y_inc = coordinates[1][1] - coordinates[0][1]

    index = 1
    while index <= len(coordinates) -1:
        if coordinates[index][0] - coordinates[index-1][0] != x_inc:
            if coordinates[index][1] - coordinates[index - 1][1] != y_inc:
                return False
            else:
                index += 1
        else:
            index += 1

    return True


c =[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates =[[2,4],[2,5],[2,8]]

print(checkStraightLine(coordinates))