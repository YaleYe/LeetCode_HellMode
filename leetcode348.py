class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n] * n

    def move(self, row: int, col: int, player: int):
        board = self.board
        n = self.n
        board[row][col] = player


        def checkRow(r):
            for row in range(0,n):
                if board[r][row] != player:
                    return False
            return True

        def checkCol(c):
            for column in range(0,n):
                if board[column][c] != player:
                    return False
            return True

        def checkDia():
            for i in range(0,n):
                if board[i][i] != player:
                    return False
            return True

        def checkAnti():
            for i in range(0,n):
                if board[i][n-i-1] != player:
                    return False
            return True

        for i in range(0,n):
            if checkRow(row):
                return player

        for d in range(0,n):
            if checkCol(col):
                return player

        checkDia()
        checkAnti()


        checkRow(row)
        checkCol(col)
        checkDia()



def __init__(self, n: int):
    self.n = n
    self.r = [0] * n
    self.c = [0] * n
    self.diag = [0, 0]


def move(self, row: int, col: int, player: int) -> int:
    score = 1 if player == 1 else -1
    self.r[row] += score
    self.c[col] += score
    if row == col:
        self.diag[0] += score
    if row + col == self.n - 1:
        self.diag[1] += score
    for s in (self.r[row], self.c[col], *self.diag):
        if abs(s) == self.n:
            return 1 if s > 0 else 2
    return 0

