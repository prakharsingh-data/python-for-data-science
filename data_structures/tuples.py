# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Tuple:")
print(fruits)

# Access elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Length
print("\nTotal fruits:", len(fruits))

# Loop through tuple
print("\nPrinting all fruits:")
for fruit in fruits:
    print(fruit)

# Count occurrences
numbers = (1, 2, 3, 2, 4, 2)
print("\nCount of 2:", numbers.count(2))

# Find index
print("Index of Mango:", fruits.index("Mango"))