# Task 21: Write a Python program to check if a number entered by the user is an Armstrong number

def is_armstrong_number(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits

try:
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
