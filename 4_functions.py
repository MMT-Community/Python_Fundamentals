# 1. Basic Function Definition and Calling
def greet(name):
    return f"Hello, {name}!"

# 2. Parameters: Default, Positional, and Keyword
def user_info(name, age, city="Unknown", country="Unknown"):
    return f"Name: {name}, Age: {age}, Lives in: {city}, {country}"


# 3. Lambda Function
sum = lambda x, y: x + y

print(sum(10, 9))