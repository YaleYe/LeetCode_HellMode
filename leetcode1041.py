def isRobotBounded(instructions):
    x,y = 0,0
    dirX, dirY = 0,1


    for letter in instructions:

        if letter == "G":
            x += dirX
            y += dirY

        elif letter == "L":
            dirX, dirY = -dirY, dirX

        elif letter == "R":
            dirX,dirY = dirY, -dirX

    return (x,y) == (0,0) or (dirX,dirY) != (0,1)

instructions = "GG"

print(isRobotBounded(instructions))