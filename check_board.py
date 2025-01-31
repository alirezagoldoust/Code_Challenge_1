def checked_board(a):
    rows = len(a)
    cols = len(a[0])

    for i in range(rows):  # پیمایش ردیف‌ها
        for j in range(cols):  # پیمایش ستون‌ها
            # لیست‌هایی برای ذخیره خانه‌های متوالی
            sliced_list1 = []
            sliced_list2 = []
            sliced_list3 = []
            sliced_list4 = []

            # بررسی ۴ خانه متوالی در هر جهت
            for k in range(4):
                # بررسی ردیف افقی (به شرطی که j + k از اندازه‌ی ستون‌ها بیشتر نشود)
                if j + k < cols:
                    sliced_list1.append(a[i][j + k])
                # بررسی ستون عمودی (به شرطی که i + k از اندازه‌ی ردیف‌ها بیشتر نشود)
                if i + k < rows:
                    sliced_list2.append(a[i + k][j])
                # بررسی قطر معکوس (به شرطی که i + k و j - k در محدوده باشند)
                if i + k < rows and j - k >= 0:
                    sliced_list3.append(a[i + k][j - k])
                # بررسی قطر اصلی (به شرطی که i + k و j + k در محدوده باشند)
                if i + k < rows and j + k < cols:
                    sliced_list4.append(a[i + k][j + k])

            # بررسی اگر چهار خانه مشابه باشند
            if len(set(sliced_list1)) == 1 and sliced_list1[0] != 0:
                return sliced_list1[0]
            if len(set(sliced_list2)) == 1 and sliced_list2[0] != 0:
                return sliced_list2[0]
            if len(set(sliced_list3)) == 1 and sliced_list3[0] != 0:
                return sliced_list3[0]
            if len(set(sliced_list4)) == 1 and sliced_list4[0] != 0:
                return sliced_list4[0]

    return 0  # اگر هیچ برنده‌ای پیدا نشد


# آزمایش کد با یک برد اولیه
result = checked_board(
    [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)

if result == 1:
    print("Winner is Player 1")
elif result == -1:
    print("Winner is Player 2")
else:
    print("No winner yet")
