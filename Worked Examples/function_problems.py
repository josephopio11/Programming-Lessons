def to_the_power(a, b):
    answer = a ** b
    return answer
    # print(answer)
    # print("This is a beautiful answer")


print("Enter a number:")
num1 = int(input())
print("Enter a second number:")
num2 = int(input())

answer = to_the_power(num1, num2)

print(f"{num1} to the power of {num2} is {answer}")
