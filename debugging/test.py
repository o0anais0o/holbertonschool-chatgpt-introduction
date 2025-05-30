#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1

            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
    