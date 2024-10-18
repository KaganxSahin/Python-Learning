
# Errors can halt program execution. Python allows us to use try-except blocks to catch and handle errors.

# Simple try-except block
try:
    result = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Error: Division by zero!")

# try-except-finally block
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found!")
finally:
    # File closure
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file to close.")
