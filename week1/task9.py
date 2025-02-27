# Task 9. Write a Python program that asks the user to enter a number and checks if it is a prime number

num = input("Enter a number: ")
try:
    num = int(num)
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        is_prime = True  # Assume the number is prime initially

        # Loop from 2 to the square root of the number (optimized check)
        # Any factor of `num` must be ≤ sqrt(num), reducing iterations
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # If num is divisible by i, it's not prime
                is_prime = False
                break  # Exit loop early since we found a factor

        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

