def check_board(a):
    for i in range(6):
        for j in range(7):
            sliced_list1 = []
            sliced_list2 = []
            sliced_list3 = []
            sliced_list4 = []

            for k in range(4):
                if j + k < 7:
                    sliced_list1.append(a[i][j + k])
                if i + k < 6:
                    sliced_list2.append(a[i + k][j])
                if i + k < 6 and j - k >= 0:
                    sliced_list3.append(a[i + k][j - k])
                if i + k < 6 and j + k < 7:
                    sliced_list4.append(a[i + k][j + k])

            for sliced_list in [sliced_list1, sliced_list2, sliced_list3, sliced_list4]:
                if len(sliced_list) == 4 and all(x == 1 for x in sliced_list):
                    print("Winner is player 2 (1)")
                    return True
                elif len(sliced_list) == 4 and all(x == -1 for x in sliced_list):
                    print("Winner is player 1 (2)")
                    return True

    return False
