# 1 - Take user input [number 1, number 2, operation]
# 2 - check the operation 
# 3 - perform the operation



num1 = int(input("Enter first number: ")) 
operation = input("Enter The Operation: ")
num2 = int(input("Enter second number: "))

if operation == "+":
  print(num1 + num2)
elif operation == "-":
  print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "/":
  print(num1 / num2)
else:
  print("Invalid Operation")
