import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Algorithm
def is_valid(board, row, col, num):
    # Check if the number is not already in the row, column or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Tkinter GUI
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center')
                self.cells[row][col].grid(row=row, column=col)
        
    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, sticky="nsew")
        
    def solve_puzzle(self):
        self.get_board_values()
        if solve_sudoku(self.board):
            self.update_grid()
        else:
            messagebox.showinfo("No Solution", "This puzzle cannot be solved.")
        
    def get_board_values(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[row][col].get()
                if value.isdigit():
                    self.board[row][col] = int(value)
                else:
                    self.board[row][col] = 0
    
    def update_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board[row][col]))

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
