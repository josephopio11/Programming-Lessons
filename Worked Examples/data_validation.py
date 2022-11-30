not_number = True

while not_number:
    try:
        print("Enter a number:")
        number = int(input())
        not_number = False
    except ValueError:
        print("Please enter a number:")

print(f"Number {number} entered correctly")
