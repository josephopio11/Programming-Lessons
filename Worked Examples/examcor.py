def linearSearch(searchValue):
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
    return False


def bubbleSort(theArray):
    for x in range(10):
        for y in range(9):
            if theArray[y] > theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp
    return theArray


arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

print(bubbleSort(arrayData))

# print("Please enter a search value: ")
# value_searched = int(input())
#
# reply_for_user = linearSearch(value_searched)
#
# if reply_for_user:
#     print("Number was found")
# else:
#     print("Number not found")
