def binary_search(items, search_item):
    index = -1
    first = 0
    last = len(items) - 1
    found = False
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            index = midpoint
            found = True
        elif items[midpoint] < search_item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    if index == -1:
        return "Missing"
    return index


list_of_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
sought_for = 70

print(binary_search(list_of_items, sought_for))

list_of_names = ["Ali", "Jane", "Juma", "Mike", "Tom", "Yan"]
indiscipline_student = "Mike"

print(binary_search(list_of_names, indiscipline_student))
