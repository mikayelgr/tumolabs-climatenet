# Task 7. This program prints the multiplication table for a number entered by the user. It prompts the user to input a number and then prints the multiplication results for that number from 1 to 10. For example, if the user enters 3, it prints the results of 3 x 1 through 3 x 10. This is a simple way to practice loops and mathematical operations in Python.

n = int(input("Enter a number to print the multiplication table for: "))
print(f"Multiplication table for {n}")
for i in range(1, 11): # Until 11 since the right endpoint is open in the definition of the range() function
    print(f"{n}*{i} = {n * i}")
