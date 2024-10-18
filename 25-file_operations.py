
# Opening and writing to a file
file_name = "example.txt"

# Opening the file in "w" mode, which creates the file if it doesn't exist or overwrites it if it does
with open(file_name, "w") as file:
    file.write("this is a test file.\n")
    file.write("Kagan Sahin\n")

print(f"Written to {file_name}.")

# Reading from the file
with open(file_name, "r") as file:
    content = file.read()
    print("File content:\n", content)

# Reading the file line by line
with open(file_name, "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # Removes any leading or trailing whitespace from each line
