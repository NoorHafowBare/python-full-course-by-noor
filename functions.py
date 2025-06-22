# Functions & Modules
# Functions are reusable blocks of code that perform a specific task. Modules are files that contain Python code (like functions and classes) which can be imported and reused.

# Defining Functions, Parameters, Return Values, and Lambda Expressions
# Defining a Function:
# A function is defined using the def keyword.

def greet(name="bare"):
    return f"hello {name}"

print(greet("Noor")) # Output: hello Noor
print(greet("hafow")) # Output: hello hafow
# If no argument is passed, it uses the default value.
print(greet()) # Output: hello bare

# Lambda Expressions:
# Lambda functions are small, anonymous functions created in a single line.
divider = lambda a,b: a / b
print(divider(10, 2)) # Output: 5.0