# Write your printing of the board functins here
# Enjoy coding and have fun!⚡️
#from apply_move import my_row
#from main import character
from pprint import pprint

    # color_codes = {
      
    #     'red'     : '\u001b[31m',
    #     'blue_bright'    : '\u001b[34;1m',
        

    #     'reset' : '\u001b[0m',
    # }

def print_mode(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j]==0):
                print(" ", end=" | ")
            elif (a[i][j]==1):
                print('\u001b[0m', '\u001b[34;1m',"●",'\u001b[0m', end=" | ", sep='')
            elif (a[i][j]==2):
                print('\u001b[0m','\u001b[31m',"●",'\u001b[0m',end=" | ",sep='')
            
        print()
        print("-"*26)

#a = [['#' for i in range(7)] for j in range(6)]
print(print_mode(a))





