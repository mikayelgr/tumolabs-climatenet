# Task 18. Write a Python program that takes three numbers from the user and prints the maximum of them

n_list = []
for i in range(0, 3):
    n_list.append(int(input("Enter a number: ")))

print(f"The maximum number from the list {n_list} is: {max(n_list)}")

