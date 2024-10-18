
# Defining a simple function
def greet():
    print("Hello, welcome to learning Python functions!")

# A function that takes a parameter
def greet_person(name):
    print(f"Hello, {name}! Welcome to learning Python functions!")

# Function with multiple parameters and default arguments
def introduction(name, age=20, language="Python"):
    print(f"Hi, my name is {name}. I am {age} years old and I am learning {language}.")

# Function that returns a value
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Calling the simple function
    greet()

    # Calling the function with a parameter
    greet_person("Kagan")

    # Calling the function with default arguments
    introduction("")
    
    # Calling the function with all arguments
    introduction("", 30, "Python")
    
    # Getting the return value from the function
    result = add_numbers(5, 10)
    print(f"The sum of 5 and 10 is: {result}")
