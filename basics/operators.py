# Operators in Python

a = 15
b = 4

print("a =", a)
print("b =", b)

# Arithmetic Operators
print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Assignment Operators
print("\nAssignment Operators")
x = 10
print("Initial x =", x)

x += 5
print("After x += 5 :", x)

x -= 3
print("After x -= 3 :", x)

x *= 2
print("After x *= 2 :", x)

# Logical Operators
print("\nLogical Operators")
age = 20
is_student = True

print(age > 18 and is_student)
print(age > 18 or False)
print(not is_student)