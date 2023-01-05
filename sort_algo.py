def bubbleSort(myList):
    n = len(myList) - 1
    NoMoreSwaps = False
    while not NoMoreSwaps:
        NoMoreSwaps = True
        for j in range(n):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
                NoMoreSwaps = False

    return myList

myNumbers = [5, 20, 100, 86, 7, 23, 6, 99, 41]
students = ["Mike", "Anita", "James", "Paul", "Ben", "Daniel", "Chris"]
print(bubbleSort(myNumbers))

print(bubbleSort(students))