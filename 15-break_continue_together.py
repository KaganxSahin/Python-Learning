# Using break and continue together
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    if number % 2 == 0:
        continue
    print(number)
