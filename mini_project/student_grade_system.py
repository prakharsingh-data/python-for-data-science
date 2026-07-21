print("===== Student Grade System =====")

name = input("Enter Student Name: ")

math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

total = math + science + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Report Card =====")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)