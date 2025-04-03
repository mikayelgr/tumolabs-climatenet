# Task 20: Write a Python program to find the greatest common divisor (GCD) of two numbers entered by the user. 

import math

def find_gcd(a, b):
    return math.gcd(a, b)

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    gcd = find_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd}")
except ValueError:
    print("Please enter valid integers.")
