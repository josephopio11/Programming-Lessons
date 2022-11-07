def insertion_sort(items):
    num_items = len(items)
    for first_unordered in range(1, num_items):
        value = items[first_unordered]
        current = first_unordered - 1
        while current >= 0 and items[current] > value:
            items[current + 1] = items[current]
            current = current - 1
        items[current + 1] = value
    return items


sample = ['Dan', 'John', 'Mike', 'Abacus', 'Cathy', 'Berry']

print(insertion_sort(sample))
