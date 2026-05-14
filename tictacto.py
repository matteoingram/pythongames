import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check for a winner or a tie."""
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return row[0]["text"]

    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]

    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]

    for row in board:
        for cell in row:
            if cell["text"] == "":
                return None

    return "Tie"

def on_click(row, col):
    """Handle a button click event."""
    global current_player

    if board[row][col]["text"] == "" and current_player:
        board[row][col]["text"] = current_player
        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    """Reset the game board."""
    global current_player
    current_player = "X"
    for row in board:
        for cell in row:
            cell["text"] = ""

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the game board
board = []
current_player = "X"

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), height=2, width=5,
                           command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

# Start the Tkinter event loop
root.mainloop()
