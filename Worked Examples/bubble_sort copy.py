def bubble_sort(items):
    num_items = len(items)
    passes = 1
    swapped = True

    while swapped == True:
        swapped = False
        for current in range(num_items - passes):
            if items[current] > items[current + 1]:
                temp = items[current]
                items[current] = items[current + 1]
                items[current + 1] = temp
                swapped = True
            print(items)
        passes = passes + 1
        # print(items)
    return items


list_of_numbers = [9, 67, 11, 6, 0, 90, 5, 1, 3, 4, 2]

print(list_of_numbers)
print(bubble_sort(list_of_numbers))
