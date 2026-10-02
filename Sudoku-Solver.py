def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == -1:
                return row, col

    return None, None

def is_valid(board, number, row, col):
    if number in board[row]:
        return False

    for i in range(9):
        if board[i][col] == number:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == number:
                return False

    return True

def solve_sudoku(board):
    row, col = find_empty_cell(board)

    if row is None:
        return True

    for number in range(1, 10):

        if is_valid(board, number, row, col):
            board[row][col] = number

            if solve_sudoku(board):
                return True

            board[row][col] = -1

    return False

board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],

    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],

    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
]

if solve_sudoku(board):
    print("Sudoku solved")

    for row in board:
        print(row)
else:
    print("No solution found")
