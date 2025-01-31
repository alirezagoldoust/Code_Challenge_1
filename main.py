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


def get_input1():
    dictionary1 = {"p1": -1}
    app_result = apply_move(dictionary1, board)
    board = app_result
    print_board(app_result)
    check_result = check_board(board)
    return check_result


def get_input2(check_result):
    dictionary2 = {"p2": 1}
    app_result = apply_move(dictionary2, board)
    board = app_result
    print_board(app_result)
    check_result = check_board(board)

    return check_result


def main():
    print_board(board)
    while True:

        if get_input1() != False:
            break

        if get_input2() != False:
            break


main()
