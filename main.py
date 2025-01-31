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
    global board
    p1_num = input("Please enter number of the column: ")
    dictionary1 = {"p1": p1_num}
    app_result = apply(dictionary1, board)
    board = app_result
    print_mode(app_result)
    check_result = checked_board(board)
    if check_result == 1:
        print("Winner is Player 1")
    elif check_result == -1:
        print("Winner is Player 2")
    else:
        print("No winner yet")


def get_input2(check_result):
    global board
    p2_num = "Please enter number of the column: "
    dictionary2 = {"p2": p2_num}
    app_result = apply(dictionary2, board)
    board = app_result
    print_mode(app_result)
    check_result = checked_board(board)
    if check_result == 1:
        print("Winner is Player 1")
    elif check_result == -1:
        print("Winner is Player 2")
    else:
        print("No winner yet")


def main():
    print_mode(board)
    while True:

        if get_input1() != False:
            break

        if get_input2() != False:
            break


main()
