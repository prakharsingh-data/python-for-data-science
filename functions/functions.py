# Functions in Python

# Function without parameters
def greet():
    print("Welcome to Python Programming!")

greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Prakhar")

# Function to add two numbers
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# Function to calculate square
def square(number):
    return number * number

num = int(input("Enter a number: "))
print("Square:", square(num))