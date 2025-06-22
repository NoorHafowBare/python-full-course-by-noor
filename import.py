# Importing and Using Modules and Packages
# Modules let you organize your code or use code written by others.

# Importing a Module:
import math # Imports the math module, which provides mathematical functions.

print(math.sqrt(16))  # Using the sqrt function from the math module

from datetime import date  # Imports only the 'date' class from the datetime module.
print(date.today())  # Prints today's date.

from datetime import time
# Imports only the 'time' class from the datetime module.
print(time()) # Prints the current time.