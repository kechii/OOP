def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get user input
student_id = input("Enter your student ID: ")
number = int(input("Enter a number to check if it's prime: "))

# Define range based on last four digits of student ID
last_four_digits = int(student_id[-4:])
start = max(2, last_four_digits - 100)
end = last_four_digits + 1000

# Check if the number is prime
if is_prime(number):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")

# Check primes in the specific range
print(f"Primes in the range {start} to {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")