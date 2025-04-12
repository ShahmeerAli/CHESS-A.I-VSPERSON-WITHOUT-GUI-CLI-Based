import random

PIECE_VALUES = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3


def find_random_move(valid_moves):
    return random.choice(valid_moves)


def find_best_move(game_state, valid_moves):
    global next_move
    next_move = None
    alpha = -CHECKMATE
    beta = CHECKMATE

    for depth in range(1, DEPTH + 1):
        alpha_beta(game_state, valid_moves, depth, alpha, beta,
                   1 if game_state.white_to_move else -1)

    return next_move if next_move else find_random_move(valid_moves)


def alpha_beta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move

    if depth == 0:
        return turn_multiplier * evaluate_board(game_state)

    max_score = -CHECKMATE
    for move in valid_moves:
        game_state.make_move(move)
        next_moves = game_state.get_valid_moves()
        score = -alpha_beta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)

        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move

        game_state.undo_move()

        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break

    return max_score


def evaluate_board(game_state):
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif game_state.stalemate:
        return STALEMATE

    score = 0

    for row in range(len(game_state.board)):
        for col in range(len(game_state.board[row])):
            square = game_state.board[row][col]
            if square != "__":
                piece_type = square[1]
                color = square[0]

                if color == 'w':
                    score += PIECE_VALUES[piece_type]
                else:
                    score -= PIECE_VALUES[piece_type]

    return score