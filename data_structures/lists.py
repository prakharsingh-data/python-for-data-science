# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)

# Access elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add an element
fruits.append("Grapes")
print("\nAfter append:")
print(fruits)

# Remove an element
fruits.remove("Banana")
print("\nAfter remove:")
print(fruits)

# Length
print("\nTotal fruits:", len(fruits))

# Loop through list
print("\nPrinting all fruits:")
for fruit in fruits:
    print(fruit)