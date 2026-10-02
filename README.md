# Sudoku Solver
A simple Sudoku solver built with Python. The program solves a Sudoku puzzle automatically by trying different numbers and using **backtracking** when a number leads to an incorrect solution.
## Features

* Solves a 9×9 Sudoku puzzle
* Checks rows, columns, and 3×3 boxes
* Uses recursive backtracking
* Displays the solved Sudoku board
* Simple and easy-to-understand Python code

## Technologies

* Python

## How It Works

The solver follows these steps:

1. Finds an empty cell in the Sudoku board.
2. Tries numbers from 1 to 9.
3. Checks if the number is valid.
4. Places the number if it is valid.
5. Calls the solver again using recursion.
6. If the number leads to a wrong solution, it removes the number and tries another one.

This process continues until the complete Sudoku is solved.

## Algorithm

**Recursive Backtracking**

The program tries a possible number, continues solving the puzzle, and goes back to the previous step if the choice does not lead to a solution.
