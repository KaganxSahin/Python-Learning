
# In Python, modules are reusable pieces of code that provide specific functionality.
# Modules can be part of Python's standard library or user-defined.

# Using the Math module
import math

# Square root and trigonometric calculations
number = 16
print(f"The square root of {number} is:", math.sqrt(number))
print("Cosine of 0 degrees:", math.cos(0))
print("Sine of 30 degrees:", math.sin(math.radians(30)))

# Using the Random module
import random

# Generating a random number
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# Creating and shuffling a random list
random_list = list(range(1, 11))  # Numbers from 1 to 10
print("Original list:", random_list)
random.shuffle(random_list)  # Shuffle the list
print("Shuffled list:", random_list)

# Importing module 
import my_module

my_module.say_hello()

# my_module.py (you need to create a file named 'my_module.py' in the same directory)

def say_hello():
    print("Hello from my_module!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
