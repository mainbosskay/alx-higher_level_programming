#!/usr/bin/python3
"""Program that solves the N queens problem"""
from sys import argv, exit


def start_board(q):
    """Initializing an NxN sized chessboard
    Args: board (list): lists representing the chessboard"""
    board = []
    [board.append([]) for k in range(q)]
    [rows.append(' ') for k in range(q) for rows in board]
    return (board)


def copy_board(board):
    """Returns copy of the chessboard
    Args: board (list): lists representing the chessboard"""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return (board)


def get_queensposition(board):
    """Gets and returns solved chessboard
    Args: board (list): lists representing the chessboard"""
    sotn = []
    for t in range(len(board)):
        for d in range(len(board)):
            if board[t][d] == "Q":
                sotn.append([t, d])
                break
    return (sotn)


def mark_spot(board, rows, column):
    """Marking spots non-attacking queen cannot play
    Args: board (list): chessboard
        rows (int): row queen played last
        column (int): column queen played last"""
    for d in range(column + 1, len(board)):
        board[rows][d] = "k"
    for d in range(column - 1, -1, -1):
        board[rows][d] = "k"
    for t in range(rows + 1, len(board)):
        board[t][column] = "k"
    for t in range(rows - 1, -1, -1):
        board[t][column] = "k"
    d = column + 1
    for t in range(rows + 1, len(board)):
        if d >= len(board):
            break
        board[t][d] = "k"
        d = d + 1
    d = column - 1
    for t in range(rows - 1, -1, -1):
        if d < 0:
            break
        board[t][d]
        d = d - 1
    d = column + 1
    for t in range(rows - 1, -1, -1):
        if d >= len(board):
            break
        board[t][d] = "k"
        d = d + 1
    d = column - 1
    for t in range(rows + 1, len(board)):
        if d < 0:
            break
        board[t][d] = "k"
        d = d - 1


def solve_queens(board, rows, qun, sotn):
    """Solving N-queens puzzle recursively
    Args: board (list): chessboard
        rows (int): row currently working
        qun (int): number of queens placed
        sotn (list): list of lists of solutions"""
    if qun == len(board):
        sotn.append(get_queensposition(board))
        return (sotn)
    for d in range(len(board)):
        if board[rows][d] == " ":
            tmpbrd = copy_board(board)
            tmpbrd[rows][d] = "Q"
            mark_spot(tmpbrd, rows, d)
            sotn = solve_queens(tmpbrd, rows + 1, qun + 1, sotn)
    return (sotn)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    board = start_board(int(argv[1]))
    sotn = solve_queens(board, 0, 0, [])
    for j in sotn:
        print(j)
