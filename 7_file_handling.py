# File Handling in Python

# # Writing to a text file
# with open("sample.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample text file.\n")
#     file.write("Python file handling is easy!")

# print("File 'sample.txt' has been written. 1")

# # Reading from a text file
# print("\nReading the entire file:")
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Reading line by line
# print("\nReading line by line:")
# with open("sample.txt", "r") as file:
#     for line in file:
#         print("Hi, - ", line.strip())

# # Appending to a file
# with open("sample.txt", "a") as file:
#     file.write("\nThis line is appended.")

# print("\nFile 'sample.txt' has been updated.")

# # Reading and writing binary files
# with open("binary_file.bin", "wb") as file:
#     file.write(b"\x48\x65\x6C\x6C\x6F")  # "Hello" in hexadecimal

# print("\nBinary file 'binary_file.bin' has been written.")

# with open("binary_file.bin", "rb") as file:
#     binary_content = file.read()
#     print("Binary content:", binary_content)
#     print("Decoded content:", binary_content.decode())

# Working with CSV files
# import csv

# # Writing to a CSV file
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "San Francisco"],
#     ["Charlie", 35, "London"]
# ]

# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("\nCSV file 'data.csv' has been written.")

# # Reading from a CSV file
# print("\nReading from CSV file:")
# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# # Working with JSON files
# import json

# # Writing to a JSON file
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "painting", "cycling"]
# }

# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

# print("\nJSON file 'person.json' has been written.")

# # Reading from a JSON file
# print("\nReading from JSON file:")
# with open("person.json", "r") as file:
#     loaded_person = json.load(file)
#     print(loaded_person)
