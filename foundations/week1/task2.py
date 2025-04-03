# Task 2. Ask the user to input a number and determine if the number is even or odd. If the user inputs 0, the program exits the loop. It uses the modulus operator (%) to check if the number is divisible by 2, which defines whether the number is even or odd. The program also includes error handling to ensure that only valid integers are processed.

while True:
    try:
        n = int(input("Enter a number (or zero to exit): "))
        if n == 0:
            print("Exiting...")
            break

        if n % 2 == 0:
            print(f"{n} is even")
        else:
            print(f"{n} is odd")
    except ValueError:
        print("Invalid input. Please enter a valid integer")

