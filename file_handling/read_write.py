# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Welcome to Python File Handling!\n")
    file.write("This file was created using Python.")

print("Data written successfully!")

# Reading the file
with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)