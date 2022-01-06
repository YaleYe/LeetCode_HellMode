def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """

    def change(x,y):

        # calculate neighbor
        neighbor = 0

        if x-1 >0:
            if