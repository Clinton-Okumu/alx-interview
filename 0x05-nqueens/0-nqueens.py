#!/usr/bin/python3

"""
N Queens Solver - Places N non-attacking queens on an NxN chessboard
Usage: ./0-nqueens.py N
N must be an integer >= 4
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve N Queens problem
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1, n, solutions)

            # Backtrack: remove queen from board[i][col]
            board[i][col] = 0


def solve_nqueens(n):
    """
    Main function to solve N Queens problem
    Args:
        n: Size of the board
    """
    # Initialize the chessboard
    board = [[0 for x in range(n)] for y in range(n)]

    # List to store all solutions
    solutions = []

    # Start from the first column
    solve_nqueens_util(board, 0, n, solutions)

    # Print all solutions
    for sol in solutions:
        print(sol)


def main():
    """
    Main function to handle command line arguments and program execution
    """
    # Check correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse and validate N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(n)


if __name__ == "__main__":
    main()
