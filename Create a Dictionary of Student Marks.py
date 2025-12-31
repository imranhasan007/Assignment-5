
student_marks = {
    "Aman": 85,
    "Bhavna": 92,
    "Alice": 78,
    "Salman": 88
}


name = input("Enter the student's name: ")


if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:  
    print("Student not found.")
