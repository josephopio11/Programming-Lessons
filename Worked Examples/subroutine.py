def addition(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")


def subtraction(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")


def multiplication(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")


def division(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")


print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())

print("""
    Please enter any of the following to perform your
    calculation
    
    1 - addition
    2 - subtraction
    3 - multiplication
    4 - division
""")
calculation = int(input())

if calculation == 1:
    addition(num1, num2)
elif calculation == 2:
    subtraction(num1, num2)
elif calculation == 3:
    multiplication(num1, num2)
elif calculation == 4:
    division(num1, num2)
else:
    print("Please make the correct choice")