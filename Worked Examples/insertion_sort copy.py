def insertion_sort(items):
    num_items = len(items)
    for first_unordered in range(1, num_items):
        value = items[first_unordered]
        current = first_unordered - 1
        while current >= 0 and items[current] > value:
            items[current + 1] = items[current]
            current = current - 1
        items[current + 1] = value
        print(f"==> Sorted: {items}")

    return items


it_list = [9, 67, 11, 6, 0, 90, 5, 1, 3, 4, 2]
print(it_list)
print(insertion_sort(it_list))
