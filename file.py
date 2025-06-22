#  File I/O & Exception Handling
# Working with files and handling errors are essential skills for real-world programming.

# 6.1 Reading from and Writing to Files
# Files allow your programs to read and store data persistently.

with open("example.txt", "w") as file:
    file.write("hello noor")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read() # Reads the entire file content
    print(content)  # Prints the content of the file

# Using try/except Blocks for Robust Error Handling
# When errors occur, your program can handle them gracefully rather than crashing.

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number! Please enter a valid integer.")