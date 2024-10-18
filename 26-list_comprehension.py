
# List comprehension is a concise way to create and transform lists.

# Simple list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares of numbers from 1 to 5:", squares)

# Conditional list comprehension
even_squares = [n**2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# Converting a list to another list
names = ["ABC", "ABCD", "ABCDE"]
name_lengths = [len(name) for name in names]
print("Lengths of names:", name_lengths)

# Separating even and odd numbers using list comprehension
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [n for n in mixed_numbers if n % 2 == 0]
odds = [n for n in mixed_numbers if n % 2 != 0]
print("Even numbers:", evens)
print("Odd numbers:", odds)
