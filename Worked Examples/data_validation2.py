not_number = True

while not_number:
    try:
        print("Please enter a number between 1 and 10")
        number = int(input())
        if number >= 1 and number <= 10:
            not_number = False
        else:
            print("The number you have entered is out of the range")
    except ValueError:
        print("You must enter a number between 1 and 10")

print(f"You entered the correct number: {number}")