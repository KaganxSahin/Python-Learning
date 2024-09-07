# A number guessing game that continues until the user makes the correct guess
correct_number = 7
guess = None

while guess != correct_number:
    guess = int(input("Guess a number: "))
    
    if guess < correct_number:
        print("Try a larger number.")
    elif guess > correct_number:
        print("Try a smaller number.")
    else:
        print("Congratulations! Correct guess.")
