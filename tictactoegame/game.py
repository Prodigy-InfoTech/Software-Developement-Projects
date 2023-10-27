import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
current_player = "X"
game_board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[tk.Button(root, text="", width=10, height=5, font=("Arial", 20), command=lambda row=row, col=col: on_button_click(row, col))
            for col in range(3)] for row in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)
def on_button_click(row, col):
    global current_player
    if game_board[row][col] == "":
        game_board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        buttons[row][col]["state"] = "disabled"
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
def check_winner(player):
    for i in range(3):
        if all(game_board[i][j] == player for j in range(3)):
            return True
        if all(game_board[j][i] == player for j in range(3)):
            return True
    if all(game_board[i][i] == player for i in range(3)) or all(game_board[i][2 - i] == player for i in range(3)):
        return True
    return False
def check_board_full():
    return all(game_board[i][j] != "" for i in range(3) for j in range(3))
def reset_game():
    global current_player, game_board
    current_player = "X"
    game_board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "active"
root.mainloop()