from apply_move import *
from print_board import *
from check_board import *

board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


def get_input1(board):
    dictionary1 = {"p1": -1}
    board = apply_move(dictionary1, board)
    print_board(board)
    return check_board(board)


def get_input2(board):
    dictionary2 = {"p2": 1}
    board = apply_move(dictionary2, board)
    print_board(board)
    return check_board(board)


def main():
    print_board(board)
    while True:
        if get_input1(board):
            break
        if get_input2(board):
            break


main()
