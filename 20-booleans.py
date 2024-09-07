# Defining boolean values
is_true = True
is_false = False

# Checking boolean values
print(is_true)  # Output: True
print(is_false)  # Output: False

# Boolean comparison operators
print(5 == 3)  # Output: False
print(10 != 2)  # Output: True
print(4 > 6)  # Output: False
print(20 < 5)  # Output: True

# Boolean logical operators
print(True and False)  # Output: False
print(True or False)  # Output: True
print(not True)  # Output: False

# Converting values to booleans
print(bool(5))  # Output: True
print(bool(0))  # Output: False
print(bool("Hello"))  # Output: True
print(bool(""))  # Output: False

# Using booleans in conditional statements
if is_true:
    print("The condition is true")
else:
    print("The condition is false")

# Short-circuit evaluation in conditional statements
x = 10
y = 20

if x < 15 and y > 5:
    print("Both conditions are true")

# Using booleans in loops
for i in range(10):
    if i % 2 == 0:
        print(f"Even number: {i}")
