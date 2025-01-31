from apply_move import *
from print_board import *
from check_board import *






def get_input1():
    p1=["p1"]
    player1= int( input("insert a number of row: "))
    p1 = p1.append(player1)
    app_result = apply_move(p1)
    print_result = print_board(app_result)
    print(print_result)
    check_result = check_board(print_result)
    return check_result

def get_input2(check_result):
    p2 = ["p2"]
    player2= int( input("insert a number of row: "))
    p2 = p2.append(player2)
    app_result = apply_move(p2)
    print_result = print_board(app_result)
    print(print_result)
    check_result = check_board(print_result)
    return check_result


def main():
    while True:
        get_input1()

        if get_input1 == False:

            get_input2()

main()