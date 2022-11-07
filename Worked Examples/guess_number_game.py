from random import randint
number = randint(1, 10)
guesses = 1
print("Guess a number between 1 and 10")
guess = int(input())

while guess != number and guesses < 3:
    # print(f"Guesses: {guesses}")
    guesses = guesses + 1
    print("Incorrect")
    print("Guess a number between 1 and 10")
    guess = int(input())

if guess == number:
    print("Correct")
else:
    print("Incorrect, guess limit reached3")
print(f"Number of guesses: {guesses}")
