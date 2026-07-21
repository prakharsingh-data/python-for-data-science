# Creating a dictionary
student = {
    "name": "Prakhar",
    "age": 21,
    "course": "B.Tech CSE",
    "cgpa": 8.71
}

print("Student Dictionary:")
print(student)

# Access values
print("\nName:", student["name"])
print("Course:", student["course"])

# Add a new key-value pair
student["city"] = "Ayodhya"

# Update a value
student["cgpa"] = 8.80

print("\nUpdated Dictionary:")
print(student)

# Loop through dictionary
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)