# Control Flow in Python

# Conditional statements
# name = "Ayman"

# if name == "Asmaa":
#   print("Hello, Asmaa")
# elif name == "Adel":
#   print("You are Asmaa's Brother")
# elif name == "Ayman":
#   print("You're Asmaa's Father")
# else:
#   print("I Don't Know You!!")


# For loops
# print("\nCounting from 1 to 5:")
# for i in range(1, 6):
#     print(i, end=" ")

# print("\n\nIterating over a list:")
# fruits = ["apple", "banana", "cherry"]

# for x in fruits: # 1- apple 2-banana 3- cherry
#     print(x, end=" ")


# While loops
# print("\n\nCounting down from 5:")
# count = 5
# while count > 0:
#     print(count, end=" ")
#     count -= 1

# Loop control: break, continue
# print("\n\nUsing break and continue:")
# for i in range(10):
#     if i == 3:
#         continue  # Skip 3
#     if i == 7:
#         break  # Stop at 7
#     print(i, end=" ")

# Else clause in loops
print("\n\nUsing else clause in a loop:")
for i in range(5): 
    print(i, end=" ")
else:
    print("\nLoop completed normally")
