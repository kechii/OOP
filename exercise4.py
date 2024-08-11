#creating a class
class Student:
    def __init__(self, name, age, student_id, batch_number):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.batch_number = batch_number

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Batch Number: {self.batch_number}")

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")
batch_number = input("Enter your batch number: ")

# Create an instance of the Student class
student = Student(name, age, student_id, batch_number)

# Display student information
student.display_student_info()