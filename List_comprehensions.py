#  List Comprehensions
# List comprehensions provide a concise way to create lists.

# Traditional Way vs. List Comprehension:

# Traditional Approach:
squares = []

for i in range(10):
    squares.append(i * i)
print(squares)

# List Comprehension:
squares = [i * i for i in range(10)]
print(squares)
