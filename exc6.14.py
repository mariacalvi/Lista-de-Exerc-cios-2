def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def square(x):
    return x ** 2

def double(x):
    return x * 2

composed = compose(square, double)
result = composed(5)
print("Composed function:", result)
