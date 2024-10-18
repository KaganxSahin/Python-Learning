
# Using the Math module
import math

# Calculating the square root
print("The square root of 16 is:", math.sqrt(16))

# Using the Random module
import random

# Generating a random number
print("Random number between 1 and 10:", random.randint(1, 10))

# Importing our own module (you need to create a file called 'my_module.py' in the same directory)
import my_module

my_module.say_hello()

# my_module.py
#Once you've saved this file in the same directory as your main script, the code you wrote earlier should work when you import it and call the say_hello() function.
def say_hello():
    print("Hello from my_module!")
