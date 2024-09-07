# Example 1: Generating numbers from 0 to 4
print("Example 1: Generating numbers from 0 to 4")
for i in range(5):
    print(i)
print()

# Example 2: Generating numbers from 2 to 6
print("Example 2: Generating numbers from 2 to 6")
for i in range(2, 7):
    print(i)
print()

# Example 3: Generating even numbers from 2 to 10
print("Example 3: Generating even numbers from 2 to 10")
for i in range(2, 11, 2):
    print(i)
print()

# Example 4: Generating numbers from 10 to 2 in reverse
print("Example 4: Generating numbers from 10 to 2 in reverse")
for i in range(10, 1, -1):
    print(i)
print()

# Example 5: Using range() with len()
print("Example 5: Using range() with len()")
my_list = ['a', 'b', 'c', 'd', 'e']
for i in range(len(my_list)):
    print(f"Index {i} has value {my_list[i]}")
print()
