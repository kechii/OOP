def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return {"even": even_count, "odd": odd_count}

# Get user input
student_id = input("Enter your student ID: ")
last_four_digits = int(student_id[-4:])

# Create a sample list and modify it
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
modified_list = [num + last_four_digits for num in original_list]

# Count even and odd numbers
result = count_even_odd(modified_list)

print("Original list:", original_list)
print("Modified list:", modified_list)
print("Count of even numbers:", result["even"])
print("Count of odd numbers:", result["odd"])