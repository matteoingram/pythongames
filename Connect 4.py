

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board


def print_board(board):
    print("  ".join([str(i) for i in range(COLUMN_COUNT)])) 
    for row in board:
        print("|".join(row))
        print("-" * (COLUMN_COUNT * 2 - 1))  


def drop_piece(board, col, piece):
    for row in range(ROW_COUNT-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row, col
    return None


def check_win(board, piece):
    
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    
    for row in range(3, ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
    return False

def connect_four():
    board = create_board()
    print_board(board)
    
    turn = 0
    game_over = False
    
    while not game_over:
        piece = 'X' if turn == 0 else 'O'
        print(f"Player {piece}'s turn")
        
        
        while True:
            try:
                col = int(input(f"Choose a column (0-{COLUMN_COUNT-1}): "))
                if 0 <= col < COLUMN_COUNT and board[0][col] == ' ':
                    break
                else:
                    print("Invalid column. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        
        row, col = drop_piece(board, col, piece)
        
        
        print_board(board)
        
        
        if check_win(board, piece):
            print(f"Player {piece} wins!")
            game_over = True
        
        
        if all(board[0][col] != ' ' for col in range(COLUMN_COUNT)):
            print("It's a tie!")
            game_over = True
        

        turn = 1 - turn

# Start the game
if __name__ == "__main__":
    connect_four()
