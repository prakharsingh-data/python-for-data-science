# Loops in Python

# For Loop
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# While Loop
print("\nCountdown:")
count = 5

while count > 0:
    print(count)
    count -= 1

# Sum of first 10 numbers
sum = 0

for i in range(1, 11):
    sum += i

print("\nSum of first 10 numbers:", sum)

# Multiplication Table
number = int(input("\nEnter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    