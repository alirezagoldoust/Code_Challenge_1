# Write you checking of four in row logic here
# have a great project!✨

def checked_board(a):
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

            # print(sliced_list1, int(sum(sliced_list1) / 4))
            # print(sliced_list2, int(sum(sliced_list2) / 4))
            # print(sliced_list3, int(sum(sliced_list3) / 4))
            # print(sliced_list4, int(sum(sliced_list4) / 4))
            checked = ((int(sum(sliced_list1) / 4)) +
                       (int(sum(sliced_list2) / 4)) +
                       (int(sum(sliced_list3) / 4)) +
                       (int(sum(sliced_list4) / 4)))
            if checked != 0:
                # print(checked)
                return 1 if checked > 0 else -1

            if checked >= 1:
                print("winner is player 1")
            if checked <= -1:
                print("winner is player 2")

    return 0
