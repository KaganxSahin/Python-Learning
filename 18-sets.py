# Create a set
my_set = {1, "Hello", 3.14}

# Check if an item is in the set
item_in_set = "Hello" in my_set
print(f"Is 'Hello' in the set?: {item_in_set}")

# Add an item to the set
my_set.add("World")
print(my_set)

# Remove an item from the set
my_set.remove("Hello")
print(my_set)

# Check if a set is empty
is_empty = not my_set
print(f"Is the set empty?: {is_empty}")

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

# Intersection of sets
intersection_set = set1 & set2
print(intersection_set)

# Difference of sets
difference_set = set1 - set2
print(difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

# Update a set with another set
set1.update(set2)
print(set1)

# Copy a set
my_set_copy = my_set.copy()
print(my_set_copy)

# Clear a set
my_set.clear()
print(my_set)
