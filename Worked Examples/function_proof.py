print("Welcome to the times table quiz")
not_validated = True
while not_validated:
    try:
        print("Enter a times table that you would like to be tested on:")
        times_table = int(input())
        not_validated = False
    except ValueError:
        print("You must enter a whole number: ")
not_validated = True
while not_validated:
    print("Enter the maximum value for your times table: ")
    try:
        max_value = int(input())
        not_validated = False
    except ValueError:
        print("You must enter a whole number: ")
max_value = max_value + 1
answer = 0
print(f"Here is your quiz on the {times_table} times table")
for x in range(1, max_value):
    answer = x * times_table
    print(f"{x} times {times_table} is ...")
    not_validated = True
    while not_validated:
        try:
            print("Answer:")
            user_answer = int(input())
            not_validated = False
        except ValueError:
            print("You must enter a whole number")
    if user_answer == answer:
        print("Correct")
    else:
        print("Incorrect")
