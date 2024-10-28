# Variables and Data Types in Python

# Variables are named references to stored data values
name = "Mohammed" # String (text) | كلام ( " sagasga " )
age = 30 # Integer | عدد صحيح
height = 1.75 # Float | عدد عشري  
is_student = True # Boolean | صحيح أو خاطئ  (True, False)

# print(f"Name: {name}, Type: {type(name)}")
# print(f"Age: {age}, Type: {type(age)}")
# print(f"Height: {height}, Type: {type(height)}")
# print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Python's dynamic typing system
# x = 10
# print(f"x is {x}, Type: {type(x)}")
# x = "Hello"
# print(f"x is now {x}, Type: {type(x)}")

# Common data types
# Numeric
integer_num = 42 # int => integer
float_num = 3.14 # float
complex_num = 2 + 3j # = 5

# Sequence
string_val = "Python" # str => bunch of charcters
list_val = ["Mohammed", "Ayman", 3, 4, 5, 10, 2415, 32151] # Array
tuple_val = (1, "two", 3.0)

# Mapping
dict_val = {"name": "Bob", "age": 25}

# Set
set_val = {1, 2, 3, 4, 5, 5, 5, 5, 5} # list
frozen_set_val = frozenset([1, 2, 3, 4, 5]) # Tuple

# Boolean
bool_val = True # True - False

# Type conversion
str_num = "42"
int_num = int(str_num) 
float_num = float(str_num)

print(f"String to Int: {int_num}, Type: {type(int_num)}")
print(f"String to Float: {float_num}, Type: {type(float_num)}")

# Type checking
print(f"Is 'name' a string? {isinstance(name, str)}")
print(f"Type of 'age': {type(age)}")
