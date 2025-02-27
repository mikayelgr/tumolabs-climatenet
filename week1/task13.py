# Task 13: Write a Python program that takes a number from the user and prints the multiplication table for that number. 

n = int(input("Enter a number to print the multiplication table for: "))
print(f"Multiplication table for {n}")
for i in range(1, 11): # Until 11 since the right endpoint is open in the definition of the range() function
    print(f"{n}*{i} = {n * i}")
