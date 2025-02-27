# Task 5. This program calculates the factorial of a given number. A factorial of a number n is the product of all integers from 1 to n (e.g., 5! = 5 * 4 * 3 * 2 * 1). The program uses a recursive function to compute the factorial, and it validates that the input is a non-negative integer. If the user inputs a negative number or invalid data, the program notifies them

def factorial(n: int) -> int:
    if n <= 1:
        return 1

    return n * (n - 1)

while True:
    try:
        n = int(input("Enter a number to calculate the factorial (or Ctrl+D to exit): "))
        if n < 0:
            print("The number cannot be negative")
            continue

        print(f"{n}! = {factorial(n)}")
    except ValueError:
        print("The provided value is invalid")
