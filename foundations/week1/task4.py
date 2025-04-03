# Task 4. A game where the program generates a random number between 1 and 10, and the user has to guess what the number is. The program gives hints like "Too high" or "Too low" based on the user's guess. The game continues until the user guesses the correct number, and then it displays the number of attempts taken to guess correctly. It also ensures that only valid numbers are entered.

import random

t = 0 # times attempted
n = random.randint(1, 10) # the generated random number

print("Guess the number (between 1 and 10)")

while True:
    try:
        g = int(input("Enter your guess: "))
        t += 1

        if g < 1 or g > 10:
            print("Please enter a number between 1 and 10.")
            continue

        if g < n:
            print("Too low! Try again.")
        elif g > n:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {n} in {t} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

