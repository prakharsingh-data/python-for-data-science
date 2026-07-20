# Lambda Functions in Python

# Normal function
def square(x):
    return x * x

print("Square using normal function:", square(5))

# Lambda function
square_lambda = lambda x: x * x

print("Square using lambda:", square_lambda(5))

# Lambda with two arguments
add = lambda a, b: a + b

print("Addition:", add(10, 20))

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Original List:", numbers)
print("Squared List:", squares)