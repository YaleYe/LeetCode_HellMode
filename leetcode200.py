def numIslands(grid):


    def dfs(grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1" :
            return

        grid[i][j] = "0"

        print("i:" + str(i + 1))
        print("j:" + str(j + 1))
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)
        dfs(grid, i, j + 1)

    islandNumber = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                islandNumber += 1
    print(islandNumber)


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
numIslands(grid)
