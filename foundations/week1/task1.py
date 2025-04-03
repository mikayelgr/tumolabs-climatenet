# Task: 1. Write a Python code that will repeatedly prompt the user to choose between two options: 1 and 2. If the user selects 1, they should be able to input a number, and the program will continue prompting for another choice. If the user selects 2, the program will stop the loop and display the sum of all previously inputted numbers.

sum = 0

while True:
    n = int(input("Enter an option 1 or 2: "))
    if n == 1:
        c = int(input("Enter a number: "))
        sum += c
        continue

    if n == 2:
        print(f"The sum of all numbers inputted is: {sum}")
        break
