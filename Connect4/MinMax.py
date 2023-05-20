# take the 2d array and make it using minmax and return column

import math
import random
import time

from board import Board


# minMax function to return column
def minMax(board, depth, isMaximizing):
    if depth == 0 or board.is_game_over():
        return board.evaluate()

    if isMaximizing:
        bestValue = -math.inf
        for i in range(7):
            if board.is_valid_move(i):
                board.select_column(i)
                value = minMax(board, depth - 1, False)
                board.select_column(i)
                bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = math.inf
        for i in range(7):
            if board.is_valid_move(i):
                board.select_column(i)
                value = minMax(board, depth - 1, True)
                board.select_column(i)
                bestValue = min(bestValue, value)
        return bestValue
