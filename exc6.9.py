def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i - 1)

number = 8
result = factorial(number)
print(f"The factorial of {number} is:", result)
