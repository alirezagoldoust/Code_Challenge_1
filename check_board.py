def checked_board(a):
    rows = len(a)
    cols = len(a[0])

    for i in range(rows):
        for j in range(cols):
            sliced_list1 = []
            sliced_list2 = []
            sliced_list3 = []
            sliced_list4 = []

            for k in range(4):
                if j + k < cols:
                    sliced_list1.append(a[i][j + k])
                if i + k < rows:
                    sliced_list2.append(a[i + k][j])
                if i + k < rows and j - k >= 0:
                    sliced_list3.append(a[i + k][j - k])
                if i + k < rows and j + k < cols:
                    sliced_list4.append(a[i + k][j + k])

            if len(set(sliced_list1)) == 1 and sliced_list1[0] != 0:
                return sliced_list1[0]
            if len(set(sliced_list2)) == 1 and sliced_list2[0] != 0:
                return sliced_list2[0]
            if len(set(sliced_list3)) == 1 and sliced_list3[0] != 0:
                return sliced_list3[0]
            if len(set(sliced_list4)) == 1 and sliced_list4[0] != 0:
                return sliced_list4[0]

    return 0
