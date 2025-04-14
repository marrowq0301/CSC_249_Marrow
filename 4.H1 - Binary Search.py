'''
Date:  4/6/2025
Author/Editor:  Quentin Marrow
4.H1 - Silver Attempt
'''

#4.H1 - Instructions

'''
Bronze (max 80/100 points): Recreate the binary search program from Figure 2.3.2 in Zybooks. However, your version must read the numbers in the vector from input.

Silver (max 90/100): Using the general idea of binary search (and with the 2.3.2 code as inspiration), write a program with the following requirements:
-Ask the user to choose a number from 0 to 99.
-Your program will begin by guessing "Is your number 50?" (the natural midpoint)
-The user will enter "<" if their number is lower, ">" if their number is higher, or "=" if this is their number exactly.
-The program will then adjust the high and low points (for example, if they entered ">", the new search space is 51 to 99)
-The program will guess until they get the number, or until it tries five times without guessing the number.

Gold (max 100/100): Assemble these two programs together into one program as follows:
-main() prints a menu that lets the user choose
--Binary Search Demo
--Binary Guess the Number Game
--Quit
-the chosen function runs.
-Return to main menu and let user choose again

'''

def binary_search():
    low = 0
    high = 100
    attempts = 0
    found = False

    while True:
        user_number = int(input("Choose a number from 0 to 99 and enter it here: "))
        if 0 <= user_number <= 99:
            break
        else:
            print("Error: Please enter a number between 0 and 99.")

    while attempts < 5 and low <= high:
        guess = (high + low) // 2
        print(f"Is your number {guess}?")
        user_input = input("Enter '<' if your number is lower, '>' if higher, '=' if correct: ")

        if user_input == '=':
            print(f"Guessed your number {guess} correctly in {attempts + 1} tries!")
            found = True
            break
        elif user_input == '<':
            high = guess - 1
        elif user_input == '>':
            low = guess + 1
        else:
            print("Invalid input. Please enter '<', '>', or '='.")
            continue

        attempts += 1

    if not found:
        print("Unable to guess your number in 5 tries.")

# Running the binary search guessing game
binary_search()
