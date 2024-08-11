def add_student(students, name, student_id):
    score = sum(int(digit) for digit in student_id[-4:])
    students[name] = score
    print(f"Added {name} with score {score}")

def remove_student(students, name):
    if name in students:
        del students[name]
        print(f"Removed {name}")
    else:
        print(f"{name} not found")

def display_students(students):
    if students:
        print("Student Information:")
        for name, score in students.items():
            print(f"{name}: {score}")
    else:
        print("No students in the database")

students = {}

while True:
    print("\n1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(students, name, student_id)
    elif choice == '2':
        name = input("Enter student name to remove: ")
        remove_student(students, name)
    elif choice == '3':
        display_students(students)
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again.")
    