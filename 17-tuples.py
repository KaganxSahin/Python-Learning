# Create a tuple
my_tuple = (1, "Hello", 3.14)

# Get the tuple length
tuple_length = len(my_tuple)
print(f"Tuple length: {tuple_length}")

# Access tuple elements by index
print(my_tuple[0])  # Access the first element
print(my_tuple[1])  # Access the second element
print(my_tuple[-1])  # Access the last element

# Iterate over tuple elements using a for loop
for item in my_tuple:
    print(item)

# Check if an item exists in the tuple
item_exists = "Hello" in my_tuple
print(f"Is 'Hello' in the tuple?: {item_exists}")

# Convert a list to a tuple
my_list = [1, "Hello", 3.14]
my_tuple = tuple(my_list)
print(my_tuple)

# Unpack a tuple into separate variables
a, b, c = my_tuple
print(a, b, c)

# Concatenate tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply a tuple by a number
tuple1 = (1, 2, 3)
result = tuple1 * 3
print(result)
