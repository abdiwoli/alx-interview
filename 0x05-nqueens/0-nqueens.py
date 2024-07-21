#!/usr/bin/python3
""" The N queens puzzle is the challenge """
import sys


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    def solve(row, board):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    result = []
    solve(0, [-1] * n)
    return result


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
