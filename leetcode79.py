def exist(board, word):
    def backtracking(i, j, word, board):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == word[0]:
            board[i][j] = "~"
            if (backtracking(i-1,j,word[1:],board)
                or backtracking(i+1,j,word[1:],board) \
                or backtracking(i,j-1,word[1:],board)
                or backtracking(i,j+1,word[1:],board)):
                return True
            board[i][j] = word[0]
        return False


    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            return backtracking(i,j, word, board)
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "CSE"

ans = exist(board, word)
print(ans)
