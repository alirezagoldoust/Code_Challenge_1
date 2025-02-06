from pprint import pprint


def print_mode(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                print(" ", end=" | ")
            elif a[i][j] == 1:
                print("\u001b[0m", "\u001b[34;1m", "●", "\u001b[0m", end=" | ", sep="")
            elif a[i][j] == -1:
                print("\u001b[0m", "\u001b[31m", "●", "\u001b[0m", end=" | ", sep="")

        print()
        print("-" * 26)
