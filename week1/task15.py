n_list = input("Enter a list of numbers: ").split()
s = 0
for i in range(len(n_list)):
    s += int(n_list[i])

print(f"Sum is {s}")

