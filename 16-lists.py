# Create a list
my_list = [1, "Hello", 3.14]

# Get the list length
list_length = len(my_list)
print(f"List length: {list_length}")

# Append an item to the list
my_list.append("Python")
print(my_list)

# Insert an item at a specific index in the list
my_list.insert(1, "World")
print(my_list)

# Remove an item from the list
my_list.remove("Hello")
print(my_list)

# Delete the item at a specific index
del my_list[2]
print(my_list)

# Clear the list
my_list.clear()
print(my_list)

# Copy the list
my_list_copy = my_list.copy()
print(my_list_copy)

# Reverse the list elements
my_list.reverse()
print(my_list)

# Sort the list
my_list.sort()
print(my_list)

# Sort the list in a specific order (reverse)
my_list.sort(reverse=True)
print(my_list)

# Check if an item exists in the list
element_exists = "Hello" in my_list
print(f"Is 'Hello' in the list?: {element_exists}")

# Slice a sublist
sub_list = my_list[1:3]
print(sub_list)

# Create a string by joining the list elements
list_str = ", ".join(my_list)
print(list_str)
