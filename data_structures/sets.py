# Creating a set
fruits = {"Apple", "Banana", "Mango", "Orange"}

print("Original Set:")
print(fruits)

# Add an element
fruits.add("Grapes")

# Remove an element
fruits.remove("Banana")

print("\nUpdated Set:")
print(fruits)

# Check membership
print("\nIs Mango present?", "Mango" in fruits)

# Another set
more_fruits = {"Mango", "Kiwi", "Apple"}

# Union
print("\nUnion:")
print(fruits.union(more_fruits))

# Intersection
print("\nIntersection:")
print(fruits.intersection(more_fruits))