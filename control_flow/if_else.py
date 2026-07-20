# If-Else Statements in Python

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Even or Odd
number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print(number, "is an Even number.")
else:
    print(number, "is an Odd number.")

# Grade Checker
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
