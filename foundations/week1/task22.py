# Task 22: Write a Python program that finds the second largest number in a list of numbers.

n_list = []
for i in range(0, 3):
    n_list.append(int(input("Enter a number: ")))

n_list.remove(max(n_list))

print(f"The second maximum number is: {max(n_list)}")

