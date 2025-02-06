from apply_move import *
from print_board import *
from check_board import *

board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def get_input1(board):
    column = int(input("Player 1, enter column (0-6): "))
    board = apply_move("p1", column, board)
    print_mode(board)
    return check_board(board)


def get_input2(board):
    column = int(input("Player 2, enter column (0-6): "))
    board = apply_move("p2", column, board)
    print_mode(board)
    return check_board(board)


def main():
    print_mode(board)
    while True:
        if get_input1(board):
            break
        if get_input2(board):
            break


main()
