students = ["Rahul", "Sneha", "Amit", "Priya"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

students.append("Neha")
print("After adding new student:", students)

students.remove("Amit")
print("After removing absent student:", students)