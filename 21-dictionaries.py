# Creating a dictionary
my_dict = {"key1": "value1", "key2": 2, "key3": [1, 2, 3]}

# Accessing dictionary values using keys
print(my_dict["key1"])  # Output: value1
print(my_dict["key2"])  # Output: 2
print(my_dict["key3"][1])  # Output: 2

# Adding new key-value pairs
my_dict["key4"] = "Hello"
print(my_dict)  # Output: {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3], 'key4': 'Hello'}

# Modifying existing values
my_dict["key2"] = 3.14
print(my_dict)  # Output: {'key1': 'value1', 'key2': 3.14, 'key3': [1, 2, 3], 'key4': 'Hello'}

# Checking if a key exists
if "key2" in my_dict:
    print("key2 exists in the dictionary")

# Removing key-value pairs
del my_dict["key3"]
print(my_dict)  # Output: {'key1': 'value1', 'key2': 3.14, 'key4': 'Hello'}

# Iterating over dictionary keys and values
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Getting a list of keys or values
print(list(my_dict.keys()))  # Output: ['key1', 'key2', 'key4']
print(list(my_dict.values()))  # Output: ['value1', 3.14, 'Hello']

# Checking if a dictionary is empty
if not my_dict:
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")

# Copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'key1': 'value1', 'key2': 3.14, 'key4': 'Hello'}
