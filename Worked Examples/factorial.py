def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
        print(result)
    return result


factorial(20)