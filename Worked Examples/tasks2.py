# num1 = 10
# num2 = 15
#
# print(f"First num1 = {num1}")
# print(f"First num2 = {num2}")
#
# temp = num1
# num1 = num2
# num2 = temp
#
# print(f"Second num1 = {num1}")
# print(f"Second num2 = {num2}")

#
# distance_in_miles = int(input("Enter the distance in miles: "))
#
# print(f"Distance is {distance_in_miles * 1.61} km")


# secret_number = 8
# guess = int(input("Guess the number: "))
# if guess == secret_number:
#     print("Well done")
# elif guess > secret_number:
#     print("Secret number is smaller")
# else:
#     print("Secret number is greater")


name = input("Enter name: ")
age = int(input("Enter age: "))

if name == "Queen":
    if age >= 18:
        print("Hello your Majesty, may I serve you drink?")
    else:
        print("I'm sorry your Majesty, you are too young to buy a drink")
else:
    if age >= 18:
        print("Hello mate, can I serve you drink?")
    else:
        print("Get out of my pub, you are too young to buy drink")
