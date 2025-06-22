# Data Structures
# Data structures allow us to organize and store data in various ways. We’ll cover lists, tuples, sets, and dictionaries.

# Lists, Tuples, Sets, Dictionaries
# Lists:
# Ordered and mutable (changeable) collections of items.

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
fruits.append("orange")  # Adding an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")  # Removing an item
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Tuples:
# Ordered and immutable (unchangeable) collections of items.
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Sets:
# Unordered collections of unique items.
unique_numbers = {1, 2, 3, 4, 5, 2, 3}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
unique_numbers.add(6)  # Adding an item
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}
unique_numbers.remove(3)  # Removing an item
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Dictionaries:
# Collections of key-value pairs.
person = {"name": "Noor", "age": 25, "phone": "+254743789242"}
print(person)  # Output: {'name': 'Noor', 'age': 25, 'phone': '+254743789242'}
print(person["name"])  # Output: Noor
print(person["age"])  # Output: 25

person["city"] = "Nairobi"  # Adding a new key-value pair
print(person)  # Output: {'name': 'Noor', 'age': 25, 'phone': '+254743789242', 'city': 'Nairobi'}
del person["age"]  # Removing a key-value pair
print(person)  # Output: {'name': 'Noor', 'phone': '+254743789242', 'city': 'Nairobi'}
