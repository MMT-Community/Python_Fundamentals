# Modules and Packages in Python

# Importing built-in modules
import math
import random
from datetime import datetime

# Using imported modules
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number between 1 and 10: {random.randint(1, 10)}")
print(f"Current date and time: {datetime.now()}")

# Importing the custom module
import Modules.my_module as mod

print(f"\nUsing custom module:")
print(mod.greet("Alice"))
print(f"5 + 3 = {mod.add(5, 3)}")
print(f"PI value: {mod.PI}")

# Importing specific items from a module
from Modules.my_module import greet, PI

print(f"\nUsing specific imports:")
print(greet("Bob"))
print(f"PI value: {PI}")
