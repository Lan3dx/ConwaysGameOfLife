from settings import *

def calculate(board, height, width):
    count = 0

    try: 
        if board[height-1][width-1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height-1][width+1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height][width-1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height][width+1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height+1][width-1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height+1][width] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height+1][width+1] == SYMBOL: count += 1
    except IndexError: pass

    try: 
        if board[height-1][width] == SYMBOL: count += 1
    except IndexError: pass

    return count