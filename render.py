def out(board):

    for height in range(len(board)):

        for width in range(len(board[height])):

            print(board[height][width], end="")

        print()