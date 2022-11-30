# Code 1 done

# class Book:
#     def __init__(self, title, author, ref_number, loan, due_date, requested):
#         self.title = title
#         self.author = author
#         self.ref_number = ref_number
#         self.loan = loan
#         self.due_date = due_date
#         self.requested = requested
#
#     def print_book(self):
#         print(self.title, self.author, self.ref_number, self.loan, self.due_date, self.requested)
#
#
# my_book = Book("1984","Jane",234567,True,"12/12/2022","Yes")
#
# my_book.print_book()


# Code 2 Done

# fizz = 3
# buzz = 5
#
# for i in range(1, 16):
#     if i % fizz == 0 and i % buzz == 0:
#         print("FizzBuzz")
#     elif i % fizz == 0:
#         print("Fizz")
#     elif i % buzz == 0:
#         print("Buzz")
#     else:
#         print(i)


number = 1
fizz = 3
buzz = 5
playing = number < 16

while playing:
    if number % fizz == 0 and number % buzz == 0:
        print("FizzBuzz")
    elif number % buzz == 0:
        print("Buzz")
    elif number % fizz == 0:
        print("Fizz")
    else:
        print(number)
    number = number + 1
    playing = number < 16


stored_pass = "password"
password = ""
pass_mismatch = stored_pass != password

while pass_mismatch:
    print("Enter your password:")
    password = input()
    pass_mismatch = stored_pass != password

print("Access granted")
