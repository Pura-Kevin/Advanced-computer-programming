import itertools

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)

def is_draw(board):
    return all(space != " " for space in board)

def tic_tac_toe():
    board = [" "] * 9
    players = itertools.cycle(["X", "O"])

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1–9 like this:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        current_player = next(players)
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")

        if not move.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            players = itertools.cycle([current_player, "O" if current_player == "X" else "X"])
            continue

        move = int(move) - 1

        if move < 0 or move > 8:
            print("Invalid position. Choose a number from 1 to 9.")
            players = itertools.cycle([current_player, "O" if current_player == "X" else "X"])
            continue

        if board[move] != " ":
            print("That spot is already taken. Try again.")
            players = itertools.cycle([current_player, "O" if current_player == "X" else "X"])
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()