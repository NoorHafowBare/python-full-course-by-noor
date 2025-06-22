# String Manipulation and Formatting
# Strings represent text, and there are many ways to work with them.


# String concatenation
greeting = "Hello"
name = "Noor"
print(greeting + " " + name)  # Output: Hello Noor

# String formatting using f-strings (Python 3.6+)
message = f"{greeting} {name}"
print(message)  # Output: Hello Noor

# String methods: built-in functions that change the string's appearance.
# Convert to uppercase
uppercase_name = name.upper()
print(uppercase_name)  # Output: NOOR
# Convert to lowercase
lowercase_name = name.lower()
print(lowercase_name)  # Output: noor
# Capitalize the first letter
capitalized_name = name.capitalize()
print(capitalized_name)  # Output: Noor
# Replace a substring
replaced_message = message.replace("Noor", "Hafow")
print(replaced_message)  # Output: Hello Hafow
# Split a string into a list
words = message.split()
print(words)  # Output: ['Hello', 'Noor']
