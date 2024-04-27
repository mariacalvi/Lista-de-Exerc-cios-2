def fibonacci(n):
    if n <= 0:
        return "Invalid input. Must be a integer number"
    elif n == 1:
        return 0 
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


term_number = 8
result = fibonacci(term_number)
print(f"{result} is the {term_number}th term of the Fibonacci sequence")
