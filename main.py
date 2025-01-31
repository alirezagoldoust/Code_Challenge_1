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
    p1 = ["p1"]
    player1 = int(input("insert a number of culumn: "))
    p1 = p1.append(player1)
    app_result = apply_move(p1, board)
    """
    board = app_result
    print_board(app_result)
    check_result = check_board(board)
    return check_result
    """
    return app_result
    """
def get_input2(check_result):
    p2 = ["p2"]
    player2 = int(input("insert a number of culumn: "))
    p2 = p2.append(player2)
    app_result = apply_move(p2, board)
    """
    board = app_result
    print_board(app_result)
    check_result = check_board(board)

    return check_result
    """
    """

    return app_result


"""
def main():
    print_board(board)
    while True:

        if get_input1() != False:
            break

        if get_input2() != False:
            break


main()
"""


get_input1()
