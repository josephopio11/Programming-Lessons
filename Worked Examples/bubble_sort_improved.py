def bubble_sort(items):
    num_items = len(items)
    passes = 1
    swapped = True
    while swapped:
        swapped = False
        for current in range(num_items - passes):
            if items[current] > items[current + 1]:
                temp = items[current]
                items[current] = items[current + 1]
                items[current + 1] = temp
                swapped = True
        passes = passes + 1
    return items


def_list = [9, 80, 7, 6, 5]

print(bubble_sort(def_list))
