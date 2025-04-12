from engine import GameState, Move
from MoveFinder import find_best_move, find_random_move


def print_board(board):
    print("  a b c d e f g h")
    print(" +-----------------+")
    for i, row in enumerate(board):
        print(f"{8 - i}|{' '.join(piece if piece != '__' else '.' for piece in row)}|{8 - i}")
    print(" +-----------------+")
    print("  a b c d e f g h")


def parse_move(move_str, board):
    try:
        start_col = ord(move_str[0]) - ord('a')
        start_row = 8 - int(move_str[1])
        end_col = ord(move_str[2]) - ord('a')
        end_row = 8 - int(move_str[3])

        if (0 <= start_row < 8 and 0 <= start_col < 8 and
                0 <= end_row < 8 and 0 <= end_col < 8):
            return Move((start_row, start_col), (end_row, end_col), board)
    except:
        pass
    return None


def main():
    game = GameState()

    while True:
        print("\nCurrent board:")
        print_board(game.board)

        if game.checkmate:
            print("\nCheckmate! " + ("Black" if game.white_to_move else "White") + " wins!")
            break
        elif game.stalemate:
            print("\nStalemate! Game drawn.")
            break

        if game.white_to_move:
            print("\nWhite's turn")
            move_str = input("Enter your move (e.g., 'e2e4' or 'quit'): ")
            if move_str.lower() == 'quit':
                break

            move = parse_move(move_str, game.board)
            if move and move in game.get_valid_moves():
                game.make_move(move)
            else:
                print("Invalid move! Try again.")
        else:
            print("\nAI is thinking...")
            ai_move = find_best_move(game, game.get_valid_moves())
            if not ai_move:
                ai_move = find_random_move(game.get_valid_moves())
            game.make_move(ai_move)
            print(f"AI plays: {ai_move.get_chess_notation()}")


if __name__ == "__main__":
    main()