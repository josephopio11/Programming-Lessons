def mystery(my_list, thing):
    i = -1
    num = 0
    while num < len(my_list):
        if my_list[num] == thing:
            i = num
        num = num + 1
    return i


my_test = [3, 4, 5, 2, 4, 6, 9, 0, 7, 665, 3334, 6, 5634, 23, 4, 634, 6234, 23]

print(mystery(my_test, 665))
