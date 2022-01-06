def countNegatives(grid):
    counter = 0

    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] < 0:
                counter += 1

    print(counter)


grid = [[1,-1],[-1,-1]]
countNegatives(grid)