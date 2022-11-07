print("Please enter the first number: ")

try:
    num1 = int(input())
except ValueError:
    print("An error has occurred. Please enter a number instead of words")
    num1 = int(input())


print("Please enter the second number: ")

try:
    num2 = int(input())
except ValueError:
    print("An error has occurred. Please enter a number instead of words")
    num2 = int(input())

print(type(num1))
print(type(num2))
print(type(num1+num2))
print(num1+num2)
