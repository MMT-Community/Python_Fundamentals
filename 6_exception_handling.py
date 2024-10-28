# Exception Handling in Python

# Basic try-except block
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero!")

# # Multiple except clauses
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result: {result}")
# except ValueError:
#     print("Error: Please enter a valid number!")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# # Catching multiple exceptions
# try:
#     list_example = [1, 2, 3]
#     print(list_example[5])
# except (IndexError, TypeError):
#     print("Error: List index out of range or invalid type!")

# # Using Finally
try:
    x = 10 / 1
    print(x)
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This will always execute.")


# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    user_age = validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
