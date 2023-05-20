import math

from board import Board
import time
import random
import MinMax


# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    # khaled help
    # b = Board()
    # b.board = [['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
    #            ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
    #            ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*']]
    # b.board[5][3] = 'R'
    # b.board[5][4] = 'B'
    # b.board[5][2] = 'R'
    # # MinMax.minmax(b.board, 3, 0, 0, True)
    #
    # MinMax.minimax(b.board, 3, -math.inf, math.inf, True)
    # for i in range(6):
    #     for j in range(7):
    #         print(b.board[i][j], end=" ")
    #     print()
    # end khaled help

    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)



        column = MinMax.minMax(board, 3, True)

        board.select_column(column)

        time.sleep(2)


if __name__ == "__main__":
    main()
