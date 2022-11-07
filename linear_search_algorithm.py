def linear_search(list_of_items, search_item):
    index = -1
    current = 0
    found = False

    while current < len(list_of_items) and found == False:
        if list_of_items[current] == search_item:
            index = current
            found = True
        current = current + 1
    if index == -1:
        return "Not found"
    return index


students = ['Mike', 'John', 'Peter', 'Abdi', 'Fatou']

print(linear_search(students, "Pete"))

marks = [32, 21, 45, 67, 24, 63, 98, 91, 29]

needed = 22

print(linear_search(marks, needed))
