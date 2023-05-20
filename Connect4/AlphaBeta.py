import math


def alphaBeta(board, depth, alpha, beta, isMaximizing):
    if depth == 0 or board.is_game_over():
        return board.evaluate()

    if isMaximizing:
        bestValue = -math.inf
        for i in range(7):
            if board.is_valid_move(i):
                board.select_column(i)
                value = alphaBeta(board, depth - 1, alpha, beta, False)
                board.select_column(i)
                bestValue = max(bestValue, value)
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
        return bestValue
    else:
        bestValue = math.inf
        for i in range(7):
            if board.is_valid_move(i):
                board.select_column(i)
                value = alphaBeta(board, depth - 1, alpha, beta, True)
                board.select_column(i)
                bestValue = min(bestValue, value)
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
        return bestValue