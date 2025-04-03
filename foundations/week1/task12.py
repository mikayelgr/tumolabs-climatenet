# Task 12: Write a Python program that takes a number from the user and calculates the sum of its digits. 

s = 0 # The sum
n = int(input("Enter a number: "))
c = n # Copy of n for printing
while n != 0:
    s += n % 10
    n /= 10
    n = int(n)

print(f"Sum of digits of '{c}': {s}")
