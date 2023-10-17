# Create the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    
    # Check for a draw
    if " " not in board:
        return True
    
    return False

# Main game loop
current_player = "X"
while not is_game_over(board):
    print_board(board)
    while True:
        move = input(f"Player {current_player}, enter your move (1-9): ")
        try:
            move = int(move)
            if 1 <= move <= 9 and board[move - 1] == " ":
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
    
    board[move - 1] = current_player
    current_player = "O" if current_player == "X" else "X"

# Print the final board
print_board(board)

# Check the result of the game
if " " not in board:
    print("It's a draw!")
else:
    winner = "X" if current_player == "O" else "O"
    print(f"Player {winner} wins!")
    
