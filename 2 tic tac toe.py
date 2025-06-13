
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Green Frame with Score")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.score = {"X": 0, "O": 0}

        # Green outer frame
        self.frame = tk.Frame(self.root, bg="blue", padx=5, pady=5)
        self.frame.pack(padx=10, pady=10)

        # Score & Turn display
        self.info_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.info_label.pack()
        
        self.create_board()
        self.create_controls()
        self.update_info_label()

    def create_board(self):
        board_frame = tk.Frame(self.frame, bg="black")
        board_frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    board_frame, text="", font=("Arial", 36), width=5, height=2,
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn

    def create_controls(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Reset Board", font=("Arial", 12), bg="lightblue",
                  command=self.reset_board).pack(side=tk.LEFT, padx=10)

        tk.Button(btn_frame, text="Reset Scores", font=("Arial", 12), bg="tomato",
                  command=self.reset_scores).pack(side=tk.LEFT, padx=10)

    def handle_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.current_player
            if self.check_winner(self.current_player):
                self.score[self.current_player] += 1
                self.update_info_label()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_all_buttons()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_info_label()

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)) or \
               all(self.buttons[j][i]["text"] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or \
           all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(btn["text"] != "" for row in self.buttons for btn in row)

    def disable_all_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def reset_board(self):
        self.current_player = "X"
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state=tk.NORMAL)
        self.update_info_label()

    def reset_scores(self):
        self.score = {"X": 0, "O": 0}
        self.reset_board()

    def update_info_label(self):
        self.info_label.config(
            text=f"Turn: Player {self.current_player}    Score → X: {self.score['X']} | O: {self.score['O']}"
        )

# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
