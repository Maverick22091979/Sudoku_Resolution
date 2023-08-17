def is_valid(board, row, col, num):
    # Controlla se il numero è già presente nella riga o nella colonna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Controlla se il numero è già presente nel blocco 3x3
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

# Esempio di griglia di Sudoku (0 rappresenta una casella vuota)
sudoku_board = [
    [2, 0, 6, 1, 0, 9, 8, 0, 5],
    [1, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 5, 0, 0, 6, 0, 0, 3, 0],
    [0, 0, 1, 8, 0, 3, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 2, 0, 7, 5, 0, 0],
    [0, 3, 0, 0, 1, 0, 0, 7, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 6],
    [8, 0, 4, 3, 0, 5, 1, 0, 2]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("Nessuna soluzione trovata.")