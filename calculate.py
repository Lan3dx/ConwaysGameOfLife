import moore
from settings import *
import render

def main(board):

    board1 = [[" "] * WIDTH for i in range(HEIGHT)]

    for height in range(len(BOARD)):

        for width in range(len(BOARD[height])):

            count = moore.calculate(board, height, width)

            if count == 2:
                               
                if board[height][width] == SYMBOL:
                    board1[height][width] = SYMBOL  

            if count == 3:
                
                board1[height][width] = SYMBOL
    
    return board1

def get(board):

    return main(board)