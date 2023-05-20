import math

def AlphaBeta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_terminal():
        return board.evaluate(), None
    if maximizingPlayer:
        value = -math.inf
        best_move = None
        for move in board.get_valid_moves():
            new_board = board.make_move(move)
            new_value, _ = AlphaBeta(new_board, depth - 1, alpha, beta, False)
            if new_value > value:
                value = new_value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = math.inf
        best_move = None
        for move in board.get_valid_moves():
            new_board = board.make_move(move)
            new_value, _ = AlphaBeta(new_board, depth - 1, alpha, beta, True)
            if new_value < value:
                value = new_value
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move

