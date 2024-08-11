import datetime

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")

# Get current year
current_year = datetime.datetime.now().year

# Calculate birth year
birth_year = current_year - age

# Adjust birth year based on last four digits of student ID
last_four_digits = int(student_id[-4:])
adjusted_birth_year = birth_year + (last_four_digits % 100 - 50)

# Print the message
print(f"Hello, {name}! Based on your age and student ID, you were born around {adjusted_birth_year}.")
