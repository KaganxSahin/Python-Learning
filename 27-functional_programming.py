
# Python supports functions as first-class objects, meaning we can pass functions as arguments or return them.

# Lambda function
add = lambda x, y: x + y
print("Sum of 5 and 3:", add(5, 3))

# Squaring numbers using the map() function
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares using map:", squares)

# Filtering even numbers using the filter() function
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", evens)

# Summing numbers using the reduce function
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of all numbers using reduce:", sum_of_numbers)
